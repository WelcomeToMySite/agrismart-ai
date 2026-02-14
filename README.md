# AgriSmart AI - Intelligent Farming Assistant for Rural India

[![AWS](https://img.shields.io/badge/AWS-AI%20Services-orange)](https://aws.amazon.com/)
[![Hackathon](https://img.shields.io/badge/Hackathon-AI%20for%20Bharat-green)](https://hack2skill.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🌾 Problem Statement

**Track:** AI for Rural Innovation & Sustainable Systems

Rural farmers in India face critical challenges including limited access to agricultural expertise, inefficient resource management, difficulty in early disease detection, poor market intelligence, and climate change impacts. AgriSmart AI addresses these challenges through a comprehensive AI-powered platform.

## 💡 Solution Overview

AgriSmart AI is a mobile and web platform that empowers rural farmers with:

- 🌱 **AI-Powered Crop Health Monitoring** - Disease detection using computer vision (85%+ accuracy)
- 💧 **Smart Irrigation Management** - Weather-based scheduling saves 30% water
- 📊 **Market Intelligence** - Price predictions and optimal selling recommendations
- 🗣️ **Multilingual Voice Interface** - Accessibility for low-literacy users
- ☁️ **Weather Forecasting** - Hyperlocal 7-day predictions with alerts
- 👥 **Community Platform** - Knowledge sharing among farmers and experts

## 🎯 Key Features

### 1. Crop Disease Detection
- Upload crop images via mobile app
- Real-time AI analysis using TensorFlow Lite
- Treatment recommendations in local language
- Historical health tracking

### 2. Personalized Farming Recommendations
- Crop selection based on soil, weather, and market demand
- Seasonal rotation suggestions
- Optimal planting and harvesting dates
- Real-time updates

### 3. Smart Irrigation
- Integration with IoT soil moisture sensors (optional)
- 7-day irrigation schedule predictions
- SMS/app notifications
- 20-30% water usage reduction

### 4. Market Intelligence
- Current mandi (market) prices
- 30-day price trend predictions
- Optimal selling window suggestions
- Direct buyer connections

### 5. Voice Interface
- Supports Hindi, Tamil, Telugu, Bengali, Marathi
- Voice commands for all features
- Text-to-speech responses
- Offline capability for basic queries

### 6. Weather Forecasting
- 7-day hyperlocal forecasts (80% accuracy)
- Extreme weather alerts
- Integration with farming calendar
- Historical pattern analysis

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Client Layer                            │
│  Mobile App | Web App | USSD | Voice Bot                │
└─────────────────────────────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  API Gateway (AWS)                       │
└─────────────────────────────────────────────────────────┘
                          │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
    Lambda Functions  SageMaker    AWS AI Services
                                   (Rekognition, Polly,
                                    Transcribe, Comprehend)
            │             │             │
            └─────────────┼─────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              Data Layer                                  │
│  RDS (PostgreSQL) | DynamoDB | S3 | ElastiCache         │
└─────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

### Frontend
- **Mobile:** React Native
- **Web:** React.js
- **State Management:** Redux Toolkit
- **Offline Storage:** SQLite

### Backend
- **Serverless:** AWS Lambda
- **API:** Amazon API Gateway
- **Runtime:** Node.js, Python

### AI/ML Services
- **Computer Vision:** Amazon Rekognition, Custom SageMaker models
- **NLP:** Amazon Comprehend
- **Text-to-Speech:** Amazon Polly
- **Speech-to-Text:** Amazon Transcribe
- **ML Platform:** Amazon SageMaker

### Database & Storage
- **Relational DB:** Amazon RDS (PostgreSQL)
- **NoSQL:** Amazon DynamoDB
- **Object Storage:** Amazon S3
- **Cache:** Amazon ElastiCache (Redis)

### ML Models
- **Disease Detection:** MobileNetV3 with Transfer Learning (TensorFlow)
- **Price Prediction:** LSTM Neural Network
- **Recommendation Engine:** Hybrid Collaborative Filtering

## 📁 Repository Structure

```
agrismart-ai/
├── mobile-app/              # React Native mobile application
├── web-app/                 # React.js web application
├── backend/
│   ├── lambda-functions/    # AWS Lambda functions
│   ├── ml-models/           # Machine learning models
│   └── infrastructure/      # Terraform/CloudFormation
├── docs/
│   ├── requirements.md      # Detailed requirements
│   ├── design.md            # Technical design document
│   └── api-docs/            # API documentation
├── tests/                   # Unit and integration tests
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- AWS Account
- React Native development environment

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/WelcomeToMySite/agrismart-ai.git
cd agrismart-ai
```

2. **Install mobile app dependencies**
```bash
cd mobile-app
npm install
```

3. **Install backend dependencies**
```bash
cd ../backend
pip install -r requirements.txt
```

4. **Set up AWS credentials**
```bash
aws configure
```

5. **Deploy infrastructure**
```bash
cd infrastructure
terraform init
terraform apply
```

6. **Run mobile app**
```bash
cd ../../mobile-app
npx react-native run-android  # or run-ios
```

## 📊 Expected Impact

| Metric | Target |
|--------|--------|
| **Active Farmers (Year 1)** | 100,000+ |
| **Farmer Income Increase** | 25% |
| **Water Savings** | 30% |
| **Disease Detection Accuracy** | 85%+ |
| **User Satisfaction** | 4.5+ stars |

## 💰 Implementation Cost

| Component | Cost |
|-----------|------|
| Development (6 months) | ₹15,00,000 |
| ML Model Training | ₹5,00,000 |
| AWS Infrastructure (Monthly) | ₹1,70,000 |
| Content Creation | ₹3,00,000 |
| Testing & QA | ₹2,00,000 |
| **Total Year 1** | **₹45,40,000** |

## 🗓️ Roadmap

### Phase 1: Foundation (Month 1-2)
- Team setup and AWS infrastructure
- Database design
- Mobile app skeleton

### Phase 2: Core Development (Month 3-4)
- ML model training
- Image analysis feature
- Weather integration

### Phase 3: Advanced Features (Month 5-6)
- Market intelligence
- Voice interface
- Community platform

### Phase 4: Launch (Month 7)
- Beta testing with 100 farmers
- Bug fixes and optimization
- Official launch

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Team Name:** Solution_Expert
- **Team Leader:** Subrata Pramanik
- **Team Members:** 
  - Khushi Verma [khushi.v4402@gmail.com ]
  - Harshitha N [ harshitha8426@gmail.com ]
  - Subrata Pramanik[ PMM2024003@IIITA.AC.IN ]

## 📞 Contact

- **Email:** pmm2024003@iiita.ac.in 
- **Ph no :** 9073848777

## 🙏 Acknowledgments 🙏

- AWS AI for Bharat Hackathon
- India Meteorological Department (IMD)
- Agmarknet - Agricultural Marketing Information Network
- Indian Council of Agricultural Research (ICAR)
- All farmers who provided feedback during development

---

**Built with ❤️ for Rural India by Team Solution_Expert **
