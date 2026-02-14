# Contributing to AgriSmart AI

First off, thank you for considering contributing to AgriSmart AI! It's people like you that make AgriSmart AI such a great tool for empowering rural farmers.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. By participating, you are expected to uphold this code.

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/agrismart-ai.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Push to your fork: `git push origin feature/your-feature-name`
6. Submit a Pull Request

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Node version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Contributing Code

We welcome code contributions! Here are some areas where you can help:

#### Priority Areas:
- 🌱 ML model improvements for crop disease detection
- 🗣️ Adding support for more regional languages
- 📱 Mobile app UI/UX improvements
- 🔧 Backend API optimizations
- 📝 Documentation improvements
- 🧪 Writing tests

## Development Setup

### Prerequisites

- Node.js 18+
- Python 3.9+
- React Native development environment
- AWS CLI configured
- Git

### Mobile App Setup

```bash
cd mobile-app
npm install
npx react-native run-android  # or run-ios
```

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests

```bash
# Frontend tests
cd mobile-app
npm test

# Backend tests
cd backend
pytest
```

## Pull Request Process

1. **Update documentation** - Ensure README.md and other docs reflect your changes
2. **Add tests** - Include unit tests for new features
3. **Follow code style** - Run linters before submitting
4. **Update CHANGELOG** - Add a note about your changes
5. **One feature per PR** - Keep PRs focused and manageable
6. **Provide context** - Explain what and why in your PR description

### PR Title Format

Use conventional commit format:
```
feat: add voice support for Punjabi language
fix: resolve image upload bug on Android
docs: update API documentation
test: add unit tests for disease detection
```

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## How Has This Been Tested?
Describe the tests you ran

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
```

## Style Guidelines

### JavaScript/React Native

- Use ES6+ syntax
- Follow Airbnb style guide
- Use functional components with hooks
- Use meaningful variable names
- Add JSDoc comments for functions

```javascript
/**
 * Detects disease in crop image
 * @param {string} imageUri - URI of the crop image
 * @returns {Promise<Object>} Detection results
 */
async function detectDisease(imageUri) {
  // Implementation
}
```

### Python

- Follow PEP 8 style guide
- Use type hints
- Add docstrings for functions
- Keep functions small and focused

```python
def predict_disease(image_path: str) -> dict:
    """
    Predict disease from crop image.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing disease name and confidence
    """
    # Implementation
```

### Git Commit Messages

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to..." not "moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs when relevant

Good examples:
```
feat: add Bengali voice support
fix: resolve crash on image upload
docs: update installation instructions
test: add integration tests for API
```

## Project Structure

```
agrismart-ai/
├── mobile-app/           # React Native mobile app
│   ├── src/
│   │   ├── components/   # Reusable components
│   │   ├── screens/      # Screen components
│   │   ├── services/     # API services
│   │   └── utils/        # Utility functions
│   └── tests/
├── backend/
│   ├── lambda-functions/ # AWS Lambda functions
│   ├── ml-models/        # ML model code
│   └── tests/
└── docs/                 # Documentation
```

## Testing Guidelines

- Write unit tests for all new features
- Aim for >80% code coverage
- Include integration tests for API endpoints
- Test on both Android and iOS for mobile changes
- Test with different user roles and permissions

## Documentation

- Update README.md for user-facing changes
- Update API documentation for backend changes
- Add inline comments for complex logic
- Include screenshots for UI changes
- Update architecture diagrams if needed

## Community

- Join our discussions on GitHub Issues
- Share your ideas and feedback
- Help review other contributors' PRs
- Spread the word about AgriSmart AI

## Questions?

Feel free to:
- Open an issue with the `question` label
- Email us at: pmm2024003@iiita.ac.in
- Contact team lead: Subrata Pramanik

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Project documentation
- Release notes

Thank you for making AgriSmart AI better! 🌾

---

**Team Solution_Expert**
*Building technology for rural India*
