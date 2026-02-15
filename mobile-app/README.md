# EasyAgri AI - Mobile App

React Native mobile application for iOS and Android.

## Overview

EasyAgri AI is a comprehensive mobile platform empowering rural farmers with AI-powered agricultural solutions. The app provides disease detection, smart irrigation, market intelligence, weather forecasting, and access to government schemes through an intuitive, voice-first interface designed for low-literacy users.

## Features

• 🔬 **AI-powered crop disease detection** - 85%+ accuracy using computer vision
• 💧 **Smart irrigation recommendations** - Weather-based scheduling saves 30% water
• 📊 **Real-time market prices** - Price predictions and optimal selling recommendations
• 🎤 **Multilingual voice interface** - Accessibility for low-literacy users
• 🌤️ **Weather forecasts** - Hyperlocal 7-day predictions with alerts
• 📱 **Offline capability** - Core features work without internet connection
• 👥 **Community platform** - Knowledge sharing among farmers and experts
• 🏛️ **Government schemes access** - Simplified discovery and application support
• 📍 **Location-based services** - Hyperlocal weather and market data
• 🔔 **Push notifications** - Timely alerts for weather, prices, and schemes

## Tech Stack

**Frontend:**
- React Native
- React Navigation
- Redux for state management
- AsyncStorage for offline data

**AI/ML:**
- TensorFlow Lite (on-device inference)
- AWS SageMaker (cloud-based models)

**Backend Integration:**
- AWS Amplify
- AWS Lambda functions
- AWS API Gateway
- AWS S3 for image storage

**Voice & Language:**
- AWS Polly (Text-to-Speech)
- AWS Transcribe (Speech-to-Text)
- Support for Bengali, Hindi, Tamil, Telugu, Marathi

**Database:**
- DynamoDB
- SQLite (local storage)

## Prerequisites

- Node.js 18+
- React Native development environment
- Android Studio (for Android development)
- Xcode (for iOS development - macOS only)
- AWS account with configured credentials

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/EasyAgri-AI.git
cd EasyAgri-AI/mobile-app
```

### 2. Install dependencies
```bash
npm install
# or
yarn install
```

### 3. Install iOS dependencies (macOS only)
```bash
cd ios
pod install
cd ..
```

### 4. Configure AWS Amplify
```bash
amplify pull
```

### 5. Set up environment variables
Create a `.env` file in the root directory:
```
API_URL=https://your-api-endpoint.com
AWS_REGION=ap-south-1
AWS_COGNITO_POOL_ID=your-pool-id
GOOGLE_MAPS_API_KEY=your-maps-key
```

## Running the App

### Android
```bash
npx react-native run-android
```

### iOS
```bash
npx react-native run-ios
```

## Building for Production

### Android APK
```bash
cd android
./gradlew assembleRelease
```
APK will be generated at: `android/app/build/outputs/apk/release/app-release.apk`

### iOS IPA
1. Open `ios/EasyAgriAI.xcworkspace` in Xcode
2. Select Product > Archive
3. Follow the distribution workflow

## Key Features Details

### 1. Crop Disease Detection
- Capture or upload crop images
- Real-time AI analysis using TensorFlow Lite
- Disease identification with 85%+ accuracy
- Treatment recommendations in local language
- Historical health tracking

### 2. Smart Irrigation
- Weather-based irrigation scheduling
- Soil moisture monitoring integration
- Crop-specific water requirements
- 30% water savings on average
- Push notifications for optimal irrigation times

### 3. Market Intelligence
- Real-time price updates for 50+ crops
- Price predictions using ML models
- Multi-market comparison
- Optimal selling recommendations
- Historical price trends

### 4. Weather Forecasting
- Hyperlocal 7-day forecasts
- Severe weather alerts
- Crop-specific advisories
- Rainfall predictions
- Temperature and humidity tracking

### 5. Government Schemes
- Browse 15+ central and state schemes
- AI-powered eligibility matching
- Step-by-step application guidance
- Document upload with OCR verification
- Real-time application tracking
- SMS/WhatsApp notifications

### 6. Community Platform
- Discussion forums
- Expert consultations
- Farmer-to-farmer knowledge sharing
- Real-time chat support
- Agri-FAQ library

### 7. Voice Interface
- Voice commands in 5+ Indian languages
- Text-to-speech for all content
- Hands-free navigation
- Voice-based form filling
- Accessibility for low-literacy users

## Offline Functionality

The app includes robust offline support:

- **Cached Data**: Weather forecasts, market prices, scheme information
- **Local Storage**: Crop health history, user preferences, offline forms
- **Queue Sync**: Actions queued when offline, synced when connection restored
- **Offline AI**: Disease detection works offline using on-device TensorFlow Lite
- **Auto-sync**: Automatic background sync when internet available

## Project Structure

```
mobile-app/
├── src/
│   ├── components/     # Reusable UI components
│   ├── screens/        # App screens
│   ├── navigation/     # Navigation configuration
│   ├── redux/          # State management
│   ├── services/       # API services
│   ├── utils/          # Utility functions
│   ├── assets/         # Images, fonts
│   └── config/         # App configuration
├── android/            # Android native code
├── ios/                # iOS native code
├── App.js              # Root component
└── package.json        # Dependencies
```

## Testing

### Run unit tests
```bash
npm test
```

### Run E2E tests
```bash
npm run e2e:android
npm run e2e:ios
```

## Performance Optimization

- Image compression and caching
- Lazy loading for lists
- Code splitting
- Hermes JavaScript engine enabled
- Proguard/R8 for Android builds
- Bitcode for iOS builds

## Security

- AWS Cognito for authentication
- SSL/TLS encryption for API calls
- Secure storage for sensitive data
- OAuth 2.0 implementation
- Data encryption at rest and in transit

## Localization

Supported languages:
- English
- Bengali (বাংলা)
- Hindi (हिंदी)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Marathi (मराठी)

## Troubleshooting

### Metro bundler issues
```bash
npm start -- --reset-cache
```

### Android build fails
```bash
cd android
./gradlew clean
cd ..
```

### iOS pod install fails
```bash
cd ios
pod deintegrate
pod install
cd ..
```

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Code Style

We use ESLint and Prettier for code formatting:
```bash
npm run lint
npm run format
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgments

- Built for AI for Bharat Hackathon
- Powered by AWS Cloud Services
- Innovation Partner: HAO
- Media Partner: YourStory

## Support

For support and queries:
- Email: support@easyagri-ai.com
- GitHub Issues: [Create an issue](https://github.com/YourUsername/EasyAgri-AI/issues)
- Community Forum: [Join discussions](https://community.easyagri-ai.com)

## Roadmap

**Version 2.0 (Planned)**
- Drone integration for aerial crop monitoring
- Blockchain for supply chain tracking
- AI chatbot for instant farmer queries
- Integration with IoT sensors
- Livestock management module
- Financial planning tools

---

**Built with ❤️ for Rural India | AI for Bharat Hackathon 2026**
