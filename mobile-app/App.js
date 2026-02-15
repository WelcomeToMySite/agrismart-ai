/**
 * EasyAgri-AI Mobile App
 * Entry Point
 */

import React, { useEffect } from 'react';
import {
  SafeAreaView,
  StatusBar,
  StyleSheet,
  View,
  Platform,
  LogBox,
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import SplashScreen from 'react-native-splash-screen';
import { Amplify } from 'aws-amplify';
import awsconfig from './src/aws-exports';

// Redux Store
import { store, persistor } from './src/redux/store';

// Navigation
import RootNavigator from './src/navigation/RootNavigator';

// Services
import NotificationService from './src/services/NotificationService';
import OfflineSyncService from './src/services/OfflineSyncService';

// Theme
import { ThemeProvider } from './src/theme/ThemeContext';

// Components
import LoadingScreen from './src/components/LoadingScreen';
import ErrorBoundary from './src/components/ErrorBoundary';

// Configure AWS Amplify
Amplify.configure(awsconfig);

// Ignore specific warnings
LogBox.ignoreLogs([
  'Non-serializable values were found in the navigation state',
  'Setting a timer',
]);

const App = () => {
  useEffect(() => {
    // Initialize services
    const initializeApp = async () => {
      try {
        // Initialize notifications
        await NotificationService.initialize();
        
        // Initialize offline sync
        await OfflineSyncService.initialize();
        
        // Hide splash screen
        if (Platform.OS === 'android') {
          SplashScreen.hide();
        }
      } catch (error) {
        console.error('App initialization error:', error);
      }
    };

    initializeApp();

    // Cleanup
    return () => {
      NotificationService.cleanup();
      OfflineSyncService.cleanup();
    };
  }, []);

  return (
    <ErrorBoundary>
      <Provider store={store}>
        <PersistGate loading={<LoadingScreen />} persistor={persistor}>
          <ThemeProvider>
            <NavigationContainer>
              <SafeAreaView style={styles.container}>
                <StatusBar
                  barStyle="dark-content"
                  backgroundColor="#FFFFFF"
                />
                <RootNavigator />
              </SafeAreaView>
            </NavigationContainer>
          </ThemeProvider>
        </PersistGate>
      </Provider>
    </ErrorBoundary>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
});

export default App;
