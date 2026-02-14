# Design Document - EasyAgri AI

## 1. System Architecture

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                            │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ Mobile App   │ Web App      │ USSD Service │ Voice Bot      │
│ (React Native│ (React.js)   │ (Feature     │ (Amazon Connect│
│              │              │  Phones)     │                │
└──────────────┴──────────────┴──────────────┴────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (AWS)                         │
│  - Authentication & Authorization                            │
│  - Rate Limiting & Throttling                                │
│  - Request/Response Transformation                           │
└─────────────────────────────────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
┌─────────────────┐ ┌────────────┐ ┌──────────────┐
│ Lambda Functions│ │ SageMaker  │ │ AWS AI       │
│ - Image Upload  │ │ - Disease  │ │ Services     │
│ - User Mgmt     │ │   Detection│ │ - Rekognition│
│ - Recommendations│ │ - Price    │ │ - Polly      │
│ - Notifications │ │   Prediction│ │ - Transcribe │
└─────────────────┘ └────────────┘ │ - Comprehend │
                                   └──────────────┘
            │              │              │
            └──────────────┼──────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                     Data Layer                               │
├──────────────┬──────────────┬──────────────┬────────────────┤
│ RDS          │ DynamoDB     │ S3           │ ElastiCache    │
│ (PostgreSQL) │ (Real-time   │ (Images,     │ (Redis)        │
│ - User Data  │  data)       │  Models)     │ - Caching      │
│ - Crop Data  │ - Sessions   │ - Backups    │ - Sessions     │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

### 1.2 Component Architecture

#### Mobile Application Layer
- **Technology Stack:**
  - Framework: React Native 0.72+
  - State Management: Redux Toolkit
  - Offline Storage: SQLite
  - Image Handling: react-native-image-picker
  - Voice: react-native-voice
  - Maps: react-native-maps

- **Key Components:**
  1. Authentication Module
  2. Camera & Image Processing
  3. Voice Command Handler
  4. Offline Data Sync
  5. Push Notification Manager
  6. Location Services

#### Backend Services Layer
- **Microservices Architecture:**
  1. **User Service** (Lambda)
     - Registration/Login
     - Profile Management
     - Subscription Handling
  
  2. **Image Analysis Service** (Lambda + SageMaker)
     - Image preprocessing
     - Disease detection
     - Pest identification
  
  3. **Recommendation Engine** (Lambda + SageMaker)
     - Crop selection
     - Planting schedule
     - Fertilizer recommendations
  
  4. **Weather Service** (Lambda)
     - Fetch IMD data
     - Process forecasts
     - Generate alerts
  
  5. **Market Intelligence Service** (Lambda)
     - Price aggregation
     - Trend analysis
     - Optimal selling time
  
  6. **Notification Service** (SNS + Lambda)
     - SMS alerts
     - Push notifications
     - Voice calls

## 2. Data Models

### 2.1 User Schema (PostgreSQL)

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    name VARCHAR(100),
    language VARCHAR(10) DEFAULT 'hi',
    state VARCHAR(50),
    district VARCHAR(50),
    village VARCHAR(100),
    farm_size DECIMAL(10,2),
    soil_type VARCHAR(50),
    subscription_tier VARCHAR(20) DEFAULT 'free',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE farms (
    farm_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(user_id),
    farm_name VARCHAR(100),
    area_hectares DECIMAL(10,2),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    soil_ph DECIMAL(3,1),
    soil_type VARCHAR(50),
    irrigation_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE crops (
    crop_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    farm_id UUID REFERENCES farms(farm_id),
    crop_type VARCHAR(50),
    variety VARCHAR(50),
    planting_date DATE,
    expected_harvest_date DATE,
    area_hectares DECIMAL(10,2),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2.2 Image Analysis Schema (DynamoDB)

```json
{
  "analysis_id": "uuid",
  "user_id": "uuid",
  "crop_id": "uuid",
  "image_url": "s3://bucket/path",
  "timestamp": "ISO-8601",
  "analysis_result": {
    "disease_detected": "boolean",
    "disease_name": "string",
    "confidence": "float",
    "severity": "string (mild/moderate/severe)",
    "affected_area_percent": "float",
    "recommendations": ["array of strings"]
  },
  "location": {
    "latitude": "float",
    "longitude": "float"
  }
}
```

### 2.3 Recommendation Schema (DynamoDB)

```json
{
  "recommendation_id": "uuid",
  "user_id": "uuid",
  "farm_id": "uuid",
  "type": "string (crop_selection/irrigation/fertilizer)",
  "timestamp": "ISO-8601",
  "valid_until": "ISO-8601",
  "recommendation": {
    "action": "string",
    "details": "string",
    "expected_benefit": "string",
    "estimated_cost": "float",
    "priority": "string (high/medium/low)"
  },
  "input_factors": {
    "soil_type": "string",
    "weather_forecast": "object",
    "market_prices": "object",
    "current_crop": "string"
  }
}
```

## 3. Machine Learning Models

### 3.1 Crop Disease Detection Model

**Model Architecture:**
- Base Model: MobileNetV3-Large (pre-trained on ImageNet)
- Custom Classification Head: 3 Dense Layers
- Output: 50+ disease classes + healthy class
- Framework: TensorFlow 2.x

**Training Details:**
- Dataset: 100,000+ labeled images (PlantVillage + custom)
- Augmentation: Rotation, flip, zoom, brightness adjustment
- Training: Transfer learning with fine-tuning
- Validation Split: 80-10-10 (train-val-test)
- Accuracy Target: >85% on test set

**Deployment:**
- Mobile: TensorFlow Lite model (<10 MB)
- Server: SageMaker endpoint for complex analysis
- Inference Time: <3 seconds on device, <10 seconds on server

**Model Code Snippet:**
```python
import tensorflow as tf
from tensorflow.keras import layers, models

def create_disease_detection_model(num_classes=51):
    base_model = tf.keras.applications.MobileNetV3Large(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    
    # Freeze base model layers
    base_model.trainable = False
    
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model
```

### 3.2 Price Prediction Model

**Model Type:** LSTM (Long Short-Term Memory) Neural Network

**Features:**
- Historical prices (30 days)
- Seasonal trends
- Weather conditions
- Festival calendar
- Supply chain disruptions

**Architecture:**
```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_price_prediction_model(sequence_length=30, n_features=10):
    model = Sequential([
        LSTM(128, return_sequences=True, input_shape=(sequence_length, n_features)),
        Dropout(0.2),
        LSTM(64, return_sequences=False),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1)  # Price prediction
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model
```

### 3.3 Recommendation Engine

**Algorithm:** Hybrid Collaborative + Content-Based Filtering

**Components:**
1. **Soil-Crop Compatibility Matrix**
   - Matches soil types with suitable crops
   - Considers pH, nutrients, drainage

2. **Weather-Based Filtering**
   - Temperature requirements
   - Rainfall patterns
   - Season matching

3. **Market Demand Analysis**
   - Recent price trends
   - Demand forecasting
   - Profitability ranking

4. **Historical Success Rate**
   - Local farmer outcomes
   - Similar soil/weather conditions

## 4. API Design

### 4.1 Authentication APIs

```
POST /api/v1/auth/register
Request:
{
  "phone_number": "+919073848777",
  "name": "Subrata Pramanik",
  "language": "hi"
}
Response:
{
  "user_id": "uuid",
  "otp_sent": true,
  "message": "OTP sent to your phone"
}

POST /api/v1/auth/verify
Request:
{
  "phone_number": "+919073848777",
  "otp": "123456"
}
Response:
{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "user_id": "uuid"
}
```

### 4.2 Image Analysis APIs

```
POST /api/v1/analysis/detect-disease
Headers: Authorization: Bearer <token>
Request: multipart/form-data
{
  "image": File,
  "crop_type": "tomato",
  "location": {
    "latitude": 28.6139,
    "longitude": 77.2090
  }
}
Response:
{
  "analysis_id": "uuid",
  "disease_detected": true,
  "disease_name": "Late Blight",
  "confidence": 0.92,
  "severity": "moderate",
  "recommendations": [
    "Apply copper-based fungicide",
    "Remove infected leaves",
    "Improve air circulation"
  ],
  "treatment_cost_estimate": 500
}
```

### 4.3 Recommendation APIs

```
GET /api/v1/recommendations/crops
Headers: Authorization: Bearer <token>
Query: farm_id=uuid&season=kharif
Response:
{
  "recommendations": [
    {
      "crop": "Rice",
      "variety": "Pusa Basmati 1121",
      "suitability_score": 0.89,
      "expected_yield": "50 quintals/hectare",
      "estimated_profit": "₹75,000",
      "water_requirement": "medium",
      "duration_days": 120
    },
    {
      "crop": "Cotton",
      "variety": "Bt Cotton",
      "suitability_score": 0.82,
      ...
    }
  ]
}

GET /api/v1/recommendations/irrigation
Headers: Authorization: Bearer <token>
Query: crop_id=uuid
Response:
{
  "next_irrigation": "2026-02-15T06:00:00Z",
  "amount_liters": 5000,
  "reason": "Soil moisture below threshold, no rain forecasted",
  "schedule_7days": [...]
}
```

### 4.4 Weather APIs

```
GET /api/v1/weather/forecast
Headers: Authorization: Bearer <token>
Query: latitude=28.6139&longitude=77.2090&days=7
Response:
{
  "location": {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "district": "Delhi"
  },
  "current": {
    "temperature": 28,
    "humidity": 65,
    "rainfall": 0,
    "wind_speed": 12
  },
  "forecast": [
    {
      "date": "2026-02-14",
      "temp_max": 30,
      "temp_min": 18,
      "rainfall_mm": 5,
      "condition": "Light rain"
    },
    ...
  ],
  "alerts": [
    {
      "type": "heavy_rain",
      "severity": "moderate",
      "message": "Heavy rainfall expected on 15th Feb"
    }
  ]
}
```

## 5. Security Architecture

### 5.1 Authentication & Authorization
- JWT-based authentication
- OTP verification via SMS (AWS SNS)
- Token expiration: Access token (1 hour), Refresh token (30 days)
- Role-based access control (Farmer, Expert, Admin)

### 5.2 Data Security
- Encryption at rest (AES-256) for RDS and S3
- Encryption in transit (TLS 1.3) for all API calls
- Secure image upload via pre-signed S3 URLs
- PII data masking in logs

### 5.3 API Security
- API Gateway request throttling (1000 requests/min per user)
- WAF rules for DDoS protection
- Input validation and sanitization
- SQL injection prevention via parameterized queries

### 5.4 Compliance
- GDPR compliance for data privacy
- Data retention policy (2 years for active users)
- Right to deletion implementation
- Audit logging for all data access

## 6. Scalability & Performance

### 6.1 Scalability Strategy
- **Horizontal Scaling:**
  - Lambda auto-scaling based on demand
  - RDS read replicas for read-heavy operations
  - CloudFront CDN for static content
  - Multi-AZ deployment for high availability

- **Caching Strategy:**
  - Redis (ElastiCache) for frequent queries
  - Cache weather data (30 min TTL)
  - Cache market prices (1 hour TTL)
  - Cache recommendations (24 hour TTL)

### 6.2 Performance Optimization
- **Database Optimization:**
  - Indexed queries on user_id, phone_number, farm_id
  - Partitioning large tables by date
  - Query optimization with EXPLAIN ANALYZE
  - Connection pooling

- **Image Processing:**
  - Client-side image compression before upload
  - S3 Transfer Acceleration for faster uploads
  - Lazy loading in mobile app
  - Thumbnail generation for listing views

### 6.3 Monitoring & Alerting
- **CloudWatch Metrics:**
  - API latency (p50, p95, p99)
  - Lambda execution time
  - Database connection pool
  - Error rates
  
- **Application Logs:**
  - Centralized logging with CloudWatch Logs
  - Error tracking with AWS X-Ray
  - Custom business metrics

- **Alerts:**
  - Email/SMS for critical errors
  - PagerDuty integration for on-call
  - Auto-remediation for common issues

## 7. Deployment Architecture

### 7.1 CI/CD Pipeline
```
GitHub → GitHub Actions → AWS CodePipeline → CodeDeploy
  │
  ├─> Build Mobile App (iOS/Android)
  ├─> Build & Test Backend (Jest + Pytest)
  ├─> Train ML Models (SageMaker)
  ├─> Deploy Lambda Functions
  └─> Update Infrastructure (Terraform)
```

### 7.2 Environment Strategy
- **Development:** Single region, smaller instances
- **Staging:** Production-like setup for testing
- **Production:** Multi-region, auto-scaling, full monitoring

### 7.3 Infrastructure as Code
- Terraform for AWS resource provisioning
- GitOps workflow for infrastructure changes
- Automated rollback on deployment failures

## 8. Cost Optimization

### 8.1 AWS Cost Breakdown (Estimated for 100K users)
- Lambda: $500/month (1M requests/day)
- RDS: $300/month (db.t3.medium)
- S3: $200/month (100GB images)
- SageMaker: $400/month (inference endpoints)
- Data Transfer: $300/month
- **Total: ~$1,700/month**

### 8.2 Cost Reduction Strategies
- Use Lambda@Edge for edge computing
- S3 Intelligent-Tiering for storage
- Reserved Instances for predictable load
- Spot Instances for batch processing
- CloudFront caching to reduce origin requests

## 9. Offline Functionality

### 9.1 Offline-First Architecture
- SQLite local database
- Sync queue for pending operations
- Conflict resolution strategy (last-write-wins)
- Background sync when connectivity restored

### 9.2 Offline Capabilities
- View crop history
- Access cached recommendations
- On-device disease detection (TFLite)
- Queue images for upload
- View weather forecast (cached)

## 10. Testing Strategy

### 10.1 Unit Testing
- Backend: Pytest (80% coverage target)
- Mobile: Jest + React Native Testing Library
- ML Models: Model accuracy tests

### 10.2 Integration Testing
- API endpoint tests
- Database integration tests
- Third-party API mocks

### 10.3 E2E Testing
- Mobile app flows (Detox)
- Critical user journeys
- Performance testing (JMeter)

### 10.4 UAT (User Acceptance Testing)
- Beta testing with 100 farmers
- Feedback collection and iteration
- Usability testing for low-literacy users

## 11. Future Technical Enhancements

- GraphQL API for efficient data fetching
- WebSocket for real-time updates
- Federated learning for privacy-preserving ML
- Edge AI for faster on-device inference
- Blockchain for supply chain traceability
- AR for crop visualization
- Drone integration for aerial monitoring
