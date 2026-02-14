# AgriSmart AI - Backend

FastAPI-based backend for AgriSmart AI platform.

## Features

- RESTful API endpoints
- AWS Lambda integration
- ML model inference
- Database management
- Authentication & authorization

## Setup

### Prerequisites

- Python 3.9+
- PostgreSQL
- Redis
- AWS CLI configured

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

### Running Locally

```bash
# Start the server
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Project Structure

```
backend/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── lambda-functions/       # AWS Lambda functions
│   ├── disease-detection/
│   ├── weather-api/
│   └── market-data/
├── ml-models/             # Machine learning models
│   ├── disease_classifier.py
│   ├── price_predictor.py
│   └── models/           # Trained model files
├── database/             # Database schemas and migrations
│   ├── models.py
│   └── migrations/
└── tests/               # Unit tests
    ├── test_api.py
    └── test_ml_models.py
```

## API Endpoints

### Health Check
```
GET /health
```

### Disease Detection
```
POST /api/v1/detect-disease
Body: {
  "image_base64": "...",
  "crop_type": "rice",
  "location": {...}
}
```

### Weather Forecast
```
GET /api/v1/weather/{location}
```

### Market Prices
```
GET /api/v1/market-prices?crop=rice&location=delhi
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_api.py
```

## Deployment

### AWS Lambda

```bash
# Package lambda function
cd lambda-functions/disease-detection
zip -r function.zip .

# Deploy using AWS CLI
aws lambda update-function-code \
  --function-name agrismart-disease-detection \
  --zip-file fileb://function.zip
```

### Docker

```bash
# Build image
docker build -t agrismart-backend .

# Run container
docker run -p 8000:8000 agrismart-backend
```

## Environment Variables

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/agrismart

# AWS
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-south-1

# Redis
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET=your_secret_key
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](../LICENSE)
