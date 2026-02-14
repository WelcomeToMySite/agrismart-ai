# AgriSmart AI - Mobile App

React Native mobile application for iOS and Android.

## Features

- 🔬 AI-powered crop disease detection
- 💧 Smart irrigation recommendations
- 📊 Real-time market prices
- 🗣️ Multilingual voice interface
- ☁️ Weather forecasts
- 📱 Offline capability

## Prerequisites

- Node.js 18+
- React Native development environment
- Android Studio (for Android)
- Xcode (for iOS, macOS only)

## Installation

```bash
# Install dependencies
npm install

# iOS only - install pods
cd ios && pod install && cd ..
```

## Running the App

### Android

```bash
npm run android
# or
npx react-native run-android
```

### iOS

```bash
npm run ios
# or
npx react-native run-ios
```

### Development Server

```bash
npm start
```

## Project Structure

```
mobile-app/
├── App.js                 # Main entry point
├── package.json          # Dependencies
├── src/
│   ├── components/       # Reusable components
│   │   ├── CameraView.js
│   │   ├── VoiceInput.js
│   │   └── WeatherCard.js
│   ├── screens/         # Screen components
│   │   ├── HomeScreen.js
│   │   ├── DiseaseDetectionScreen.js
│   │   ├── MarketPricesScreen.js
│   │   └── ProfileScreen.js
│   ├── navigation/      # Navigation setup
│   │   └── AppNavigator.js
│   ├── services/        # API services
│   │   ├── api.js
│   │   └── storage.js
│   ├── store/          # Redux store
│   │   ├── slices/
│   │   └── store.js
│   └── utils/          # Utility functions
│       ├── permissions.js
│       └── validators.js
├── android/            # Android native code
└── ios/               # iOS native code
```

## Key Dependencies

- **React Native**: Mobile framework
- **React Navigation**: Navigation library
- **Redux Toolkit**: State management
- **Axios**: HTTP client
- **React Native Voice**: Voice recognition
- **React Native Camera**: Camera access
- **SQLite**: Local database

## Building for Production

### Android

```bash
# Generate signed APK
cd android
./gradlew assembleRelease

# Output: android/app/build/outputs/apk/release/app-release.apk
```

### iOS

```bash
# Open in Xcode
open ios/AgriSmartAI.xcworkspace

# Build using Xcode: Product > Archive
```

## Testing

```bash
# Run unit tests
npm test

# Run with coverage
npm test -- --coverage

# E2E tests (if configured)
npm run e2e
```

## Configuration

Create a `.env` file:

```env
API_BASE_URL=https://api.agrismart-ai.com
AWS_REGION=ap-south-1
ENABLE_ANALYTICS=true
```

## Troubleshooting

### Metro Bundler Issues

```bash
# Clear cache
npm start -- --reset-cache
```

### Android Build Errors

```bash
cd android
./gradlew clean
cd ..
npm run android
```

### iOS Build Errors

```bash
cd ios
pod deintegrate
pod install
cd ..
npm run ios
```

## Features Guide

### Disease Detection
1. Open camera from home screen
2. Point at crop leaf
3. Capture image
4. Get AI diagnosis instantly

### Voice Commands
- Supported languages: Hindi, Bengali, Tamil, Telugu, Marathi
- Say "Check weather" or "Market prices"
- App responds in same language

### Offline Mode
- Core features work without internet
- Data syncs when connection available
- Images cached locally

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## Support

- Email: pmm2024003@iiita.ac.in
- GitHub Issues: [Report Bug](https://github.com/WelcomeToMySite/agrismart-ai/issues)

## License

MIT License - see [LICENSE](../LICENSE)
