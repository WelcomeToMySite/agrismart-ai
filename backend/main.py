"""
EasyAgri AI - Backend API Server
Main application entry point
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///easyagri.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-change-in-production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # 24 hours
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file upload

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Logging setup
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/easyagri.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('EasyAgri AI backend startup')

# Import routes
from app.routes import auth, disease_detection, irrigation, market, weather, schemes, community

# Register blueprints
app.register_blueprint(auth.bp, url_prefix='/api/auth')
app.register_blueprint(disease_detection.bp, url_prefix='/api/disease')
app.register_blueprint(irrigation.bp, url_prefix='/api/irrigation')
app.register_blueprint(market.bp, url_prefix='/api/market')
app.register_blueprint(weather.bp, url_prefix='/api/weather')
app.register_blueprint(schemes.bp, url_prefix='/api/schemes')
app.register_blueprint(community.bp, url_prefix='/api/community')


@app.route('/')
def index():
    """API root endpoint"""
    return jsonify({
        'message': 'EasyAgri AI Backend API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'auth': '/api/auth',
            'disease_detection': '/api/disease',
            'irrigation': '/api/irrigation',
            'market': '/api/market',
            'weather': '/api/weather',
            'schemes': '/api/schemes',
            'community': '/api/community'
        }
    })


@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Check database connection
        db.session.execute('SELECT 1')
        db_status = 'healthy'
    except Exception as e:
        app.logger.error(f'Database health check failed: {str(e)}')
        db_status = 'unhealthy'
    
    return jsonify({
        'status': 'healthy' if db_status == 'healthy' else 'degraded',
        'database': db_status,
        'version': '1.0.0'
    }), 200 if db_status == 'healthy' else 503


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    app.logger.error(f'Internal server error: {str(error)}')
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit exceeded"""
    return jsonify({'error': 'File size exceeds 16MB limit'}), 413


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """Handle expired JWT tokens"""
    return jsonify({
        'error': 'Token has expired',
        'message': 'Please log in again'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """Handle invalid JWT tokens"""
    return jsonify({
        'error': 'Invalid token',
        'message': 'Authentication failed'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    """Handle missing JWT tokens"""
    return jsonify({
        'error': 'Missing authorization token',
        'message': 'Please provide a valid token'
    }), 401


# Initialize database tables
with app.app_context():
    db.create_all()
    app.logger.info('Database tables created')


if __name__ == '__main__':
    # Development server
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
