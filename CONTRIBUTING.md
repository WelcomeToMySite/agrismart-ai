# Contributing to EasyAgri AI

Thank you for your interest in contributing to EasyAgri AI! We welcome contributions from the community to help improve this platform for rural farmers across India.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear descriptive title**
- **Detailed description** of the issue
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, browser, app version)

Use the bug report template:

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g. iOS, Android, Windows]
 - Version [e.g. 1.0.0]
```

### Suggesting Features

Feature suggestions are welcome! Please:

- **Check existing feature requests** to avoid duplicates
- **Provide a clear use case** for the feature
- **Explain how it benefits farmers** and aligns with our mission
- **Include mockups or examples** if possible

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes** (see commit guidelines below)
6. **Push to your fork** (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request**

## Development Setup

### Prerequisites

- Python 3.11+
- Node.js 18+ (for mobile app)
- PostgreSQL 14+
- Redis 7+
- AWS account (for full functionality)

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/YourUsername/EasyAgri-AI.git
cd EasyAgri-AI/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configurations

# Initialize database
flask db upgrade
python scripts/seed_data.py

# Run tests
pytest

# Start development server
python main.py
```

### Mobile App Setup

```bash
cd mobile-app

# Install dependencies
npm install

# iOS setup (macOS only)
cd ios && pod install && cd ..

# Run on Android
npx react-native run-android

# Run on iOS
npx react-native run-ios
```

### Web App Setup

```bash
cd web

# Install dependencies
npm install

# Start development server
npm run dev
```

## Pull Request Process

### Before Submitting

- [ ] Code follows our style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] No linting errors
- [ ] Branch is up to date with main

### PR Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issue
Fixes #(issue number)

## Testing
Describe the tests you ran and how to reproduce them

## Screenshots
If applicable, add screenshots

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests
- [ ] All tests pass
```

### Review Process

1. At least one maintainer must review and approve
2. All CI checks must pass
3. No merge conflicts
4. Documentation updated if needed
5. Maintainer will merge when ready

## Coding Standards

### Python (Backend)

**Style Guide:** PEP 8

```python
# Good
def calculate_irrigation_schedule(field_size, crop_type, weather_data):
    """
    Calculate optimal irrigation schedule.
    
    Args:
        field_size (float): Field size in hectares
        crop_type (str): Type of crop being grown
        weather_data (dict): Weather forecast data
        
    Returns:
        dict: Irrigation schedule with timings
    """
    # Implementation
    pass

# Bad
def calc(f,c,w):
    # No docstring, unclear variable names
    pass
```

**Code Formatting:**
```bash
# Format code with Black
black app/

# Check with pylint
pylint app/

# Check with flake8
flake8 app/
```

### JavaScript/React Native (Mobile App)

**Style Guide:** Airbnb JavaScript Style Guide

```javascript
// Good
const CropHealthScreen = ({ navigation }) => {
  const [image, setImage] = useState(null);
  
  const handleImageCapture = async () => {
    try {
      const result = await ImagePicker.launchCamera();
      setImage(result.uri);
    } catch (error) {
      console.error('Image capture failed:', error);
    }
  };
  
  return (
    <View style={styles.container}>
      <Button title="Capture" onPress={handleImageCapture} />
    </View>
  );
};

// Bad
const screen = (props) => {
  var img = null; // Use const/let, not var
  return <View><Button onPress={() => {/* complex logic here */}} /></View>
};
```

**Code Formatting:**
```bash
# Format code with Prettier
npm run format

# Lint with ESLint
npm run lint
```

### General Best Practices

1. **Write clear, self-documenting code**
2. **Keep functions small and focused**
3. **Use meaningful variable names**
4. **Add comments for complex logic**
5. **Handle errors gracefully**
6. **Write tests for new features**
7. **Keep dependencies up to date**
8. **Avoid code duplication**

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

### Examples

```bash
# Good commits
feat(disease-detection): add support for wheat rust detection
fix(auth): resolve token refresh issue on Android
docs(readme): update installation instructions
test(market): add unit tests for price prediction

# Bad commits
update code
fixed bug
WIP
asdf
```

### Commit Message Rules

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to..." not "moves cursor to...")
- First line should be 50 characters or less
- Reference issues and pull requests after the first line
- Use the body to explain what and why vs. how

## Testing Guidelines

### Backend Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_disease.py

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/test_disease.py::test_disease_detection
```

### Test Structure

```python
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_disease_detection(client):
    """Test disease detection endpoint"""
    # Arrange
    image_data = get_test_image()
    
    # Act
    response = client.post('/api/disease/detect', data=image_data)
    
    # Assert
    assert response.status_code == 200
    assert 'disease' in response.json
```

### Mobile App Testing

```bash
# Unit tests
npm test

# E2E tests
npm run e2e:android
npm run e2e:ios
```

### Test Coverage

- Maintain minimum 80% code coverage
- Write tests for all new features
- Update tests when modifying existing features
- Test edge cases and error conditions

## Documentation

### Code Documentation

- **Add docstrings** to all functions and classes
- **Explain complex algorithms** with comments
- **Document API endpoints** with clear descriptions
- **Keep README up to date**

### API Documentation

We use Swagger/OpenAPI for API documentation:

```python
@app.route('/api/disease/detect', methods=['POST'])
@swag_from({
    'tags': ['Disease Detection'],
    'description': 'Detect crop disease from image',
    'parameters': [
        {
            'name': 'image',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Crop image file'
        }
    ],
    'responses': {
        200: {
            'description': 'Disease detected successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'disease': {'type': 'string'},
                    'confidence': {'type': 'number'},
                    'treatment': {'type': 'string'}
                }
            }
        }
    }
})
def detect_disease():
    pass
```

### Update Documentation

When making changes:

- Update README.md if adding new features
- Update API documentation if changing endpoints
- Add/update code comments
- Update changelog

## Questions?

If you have questions:

- Check [existing issues](https://github.com/YourUsername/EasyAgri-AI/issues)
- Join our [community forum](https://community.easyagri-ai.com)
- Email us at contribute@easyagri-ai.com

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to EasyAgri AI! Together, we're helping farmers across India. 🌾

---

**Built with ❤️ for Rural India**
