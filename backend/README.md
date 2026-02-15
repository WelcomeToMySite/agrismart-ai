# EasyAgri AI - Backend

Python-based backend API server with AI/ML capabilities for agricultural intelligence.

## Overview

The EasyAgri AI backend provides RESTful APIs for crop disease detection, weather forecasting, market price prediction, irrigation recommendations, and government scheme management. Built with Flask and deployed on AWS Lambda for serverless scalability.

## Features

- 🔬 **Crop Disease Detection API** - TensorFlow-based image classification
- 💧 **Smart Irrigation Engine** - Weather-based irrigation scheduling
- 📊 **Market Price Prediction** - Machine learning price forecasting
- 🌤️ **Weather Data Integration** - Hyperlocal weather forecasts
- 🏛️ **Government Schemes API** - Scheme eligibility and application tracking
- 👥 **Community Platform API** - Forums, chat, and expert consultations
- 🔐 **Authentication & Security** - JWT-based auth with AWS Cognito
- 📦 **Database Management** - PostgreSQL (RDS) and DynamoDB
- 🚀 **Serverless Deployment** - AWS Lambda with API Gateway

## Tech Stack

**Framework:**
- Flask 3.0
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-CORS

**AI/ML:**
- TensorFlow 2.15
- scikit-learn 1.4
- NumPy, Pandas
- Pillow (image processing)

**Database:**
- PostgreSQL (AWS RDS)
- DynamoDB
- Redis (caching)

**AWS Services:**
- Lambda (serverless functions)
- SageMaker (ML model training/deployment)
- S3 (storage)
- Rekognition (image analysis)
- Polly & Transcribe (voice services)
- Comprehend (NLP)
- API Gateway

**Authentication:**
- AWS Cognito
- JWT tokens
- bcrypt (password hashing)

**APIs & Integrations:**
- OpenWeather API
- Government data portals
- SMS/WhatsApp gateway (Twilio)

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── crop.py
│   │   ├── disease.py
│   │   ├── market.py
│   │   └── scheme.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── disease_detection.py
│   │   ├── irrigation.py
│   │   ├── market.py
│   │   ├── weather.py
│   │   ├── schemes.py
│   │   └── community.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ml_service.py
│   │   ├── weather_service.py
│   │   ├── sms_service.py
│   │   └── cache_service.py
│   └── utils/
│       ├── __init__.py
│       ├── image_processor.py
│       ├── validators.py
│       └── helpers.py
├── ml_models/
│   ├── crop_disease/
│   │   ├── model.h5
│   │   └── labels.json
│   ├── price_prediction/
│   │   └── model.pkl
│   └── irrigation/
│       └── model.pkl
├── tests/
│   ├── test_auth.py
│   ├── test_disease.py
│   ├── test_market.py
│   └── test_weather.py
├── main.py
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

## Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- AWS account with configured credentials
- OpenWeather API key

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/EasyAgri-AI.git
cd EasyAgri-AI/backend
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configurations
```

Required environment variables:
```env
# Flask
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/easyagri
REDIS_URL=redis://localhost:6379/0

# AWS
AWS_REGION=ap-south-1
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
S3_BUCKET_NAME=easyagri-images
COGNITO_USER_POOL_ID=your-pool-id
COGNITO_CLIENT_ID=your-client-id

# External APIs
OPENWEATHER_API_KEY=your-api-key
TWILIO_ACCOUNT_SID=your-sid
TWILIO_AUTH_TOKEN=your-token
TWILIO_PHONE_NUMBER=your-number

# ML Models
MODEL_PATH=./ml_models
```

### 5. Initialize database
```bash
flask db upgrade
python scripts/seed_data.py
```

### 6. Download ML models
```bash
python scripts/download_models.py
```

## Running the Application

### Development Server
```bash
python main.py
```
Server will start at `http://localhost:5000`

### Production (Gunicorn)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### Docker
```bash
docker build -t easyagri-backend .
docker run -p 5000:5000 easyagri-backend
```

## API Endpoints

### Authentication
```
POST   /api/auth/register       - Register new user
POST   /api/auth/login          - User login
POST   /api/auth/refresh        - Refresh JWT token
POST   /api/auth/logout         - User logout
GET    /api/auth/verify         - Verify token
```

### Crop Disease Detection
```
POST   /api/disease/detect      - Upload image for disease detection
GET    /api/disease/history     - Get detection history
GET    /api/disease/:id         - Get specific detection details
POST   /api/disease/feedback    - Submit feedback on detection
```

### Smart Irrigation
```
POST   /api/irrigation/schedule - Get irrigation schedule
GET    /api/irrigation/recommendations - Get recommendations
POST   /api/irrigation/update   - Update field parameters
```

### Market Intelligence
```
GET    /api/market/prices       - Get current market prices
GET    /api/market/prices/:crop - Get price for specific crop
GET    /api/market/predictions  - Get price predictions
GET    /api/market/trends       - Get market trends
POST   /api/market/compare      - Compare prices across markets
```

### Weather
```
GET    /api/weather/current     - Get current weather
GET    /api/weather/forecast    - Get 7-day forecast
GET    /api/weather/alerts      - Get weather alerts
POST   /api/weather/subscribe   - Subscribe to weather alerts
```

### Government Schemes
```
GET    /api/schemes             - List all schemes
GET    /api/schemes/:id         - Get scheme details
POST   /api/schemes/check-eligibility - Check eligibility
POST   /api/schemes/apply       - Submit application
GET    /api/schemes/applications - Get user's applications
GET    /api/schemes/applications/:id - Track application status
```

### Community
```
GET    /api/community/posts     - Get community posts
POST   /api/community/posts     - Create new post
GET    /api/community/posts/:id - Get specific post
POST   /api/community/posts/:id/reply - Reply to post
POST   /api/community/ask-expert - Ask expert question
GET    /api/community/faq       - Get FAQ
```

## ML Models

### 1. Crop Disease Detection
- **Architecture:** MobileNetV2 (TensorFlow)
- **Dataset:** PlantVillage + custom dataset
- **Classes:** 38 diseases across 14 crops
- **Accuracy:** 85%+
- **Input:** 224x224 RGB image
- **Output:** Disease class + confidence + treatment

### 2. Price Prediction
- **Algorithm:** LSTM + Random Forest ensemble
- **Features:** Historical prices, weather, demand-supply
- **Prediction:** 7-day price forecast
- **Accuracy:** RMSE < 100 for most crops

### 3. Irrigation Scheduling
- **Algorithm:** Decision Tree + Weather integration
- **Features:** Soil type, crop type, weather forecast
- **Output:** Optimal irrigation schedule
- **Water Savings:** 30% average

## Testing

### Run all tests
```bash
pytest
```

### Run with coverage
```bash
pytest --cov=app --cov-report=html
```

### Run specific test file
```bash
pytest tests/test_disease.py
```

## Deployment

### AWS Lambda Deployment

1. **Install Serverless Framework**
```bash
npm install -g serverless
```

2. **Deploy**
```bash
serverless deploy --stage prod
```

3. **Update environment variables in AWS Console**

### EC2 Deployment

1. **SSH into EC2 instance**
2. **Install dependencies**
3. **Set up Nginx reverse proxy**
4. **Configure SSL with Let's Encrypt**
5. **Set up systemd service**

## Performance Optimization

- Redis caching for frequently accessed data
- Database query optimization with indexes
- Image compression before storage
- Lazy loading for ML models
- API response caching
- Connection pooling
- Async processing with Celery

## Security

- JWT-based authentication
- Password hashing with bcrypt
- Input validation and sanitization
- SQL injection prevention (SQLAlchemy ORM)
- CORS configuration
- Rate limiting
- API key management
- Encrypted data transmission (HTTPS)
- Regular security audits

## Monitoring

- CloudWatch logs and metrics
- Error tracking with Sentry
- API performance monitoring
- Database query monitoring
- Custom health check endpoint

## Environment Variables

See `.env.example` for all required environment variables.

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## Troubleshooting

### Common Issues

**Database connection error:**
```bash
# Check PostgreSQL is running
sudo service postgresql status

# Reset database
flask db downgrade
flask db upgrade
```

**ML model not loading:**
```bash
# Re-download models
python scripts/download_models.py

# Check file permissions
chmod -R 755 ml_models/
```

**Redis connection error:**
```bash
# Start Redis
sudo service redis-server start
```

## License

MIT License - see [LICENSE](../LICENSE) file for details.

## Support

- Email: backend@easyagri-ai.com
- GitHub Issues: [Create an issue](https://github.com/YourUsername/EasyAgri-AI/issues)

## Roadmap

**Version 2.0 (Planned)**
- GraphQL API
- Real-time WebSocket support
- Advanced analytics dashboard
- Multi-tenancy support
- Blockchain integration for supply chain
- Drone data processing APIs

---

**Built for AI for Bharat Hackathon**
