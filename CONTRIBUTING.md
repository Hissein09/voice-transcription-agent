````markdown
# Contribution Guidelines 🤝

Thank you for your interest in contributing to Voice Transcription Agent!

## Getting Started

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/voice-transcription-agent.git
cd voice-transcription-agent
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install dev dependencies
pip install pytest black flake8 pytest-cov
```

---

## Development Workflow

### Code Style

We follow PEP 8 with Black formatting.

```bash
# Format code
black src/

# Check style
flake8 src/

# Fix issues
black --line-length 100 src/
```

### Testing

```bash
# Run tests
pytest tests/

# With coverage
pytest --cov=src tests/
```

### Commit Messages

```bash
# Format: type(scope): description
# Examples:
git commit -m "feat(audio): add noise detection"
git commit -m "fix(budget): correct cost calculation"
git commit -m "docs: update README"
git commit -m "test: add unit tests for recorder"
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `test` - Tests
- `refactor` - Code refactoring
- `perf` - Performance improvement
- `chore` - Build, CI/CD

---

## Areas for Contribution

### 🔊 Audio Processing
- Noise reduction
- Echo cancellation
- Better VAD implementation
- Audio compression

### 🧠 Transcription
- Support for more languages
- Custom language models
- Real-time streaming
- Punctuation addition

### 🤖 Agents
- New agent integrations (Claude, Gemini, etc.)
- Agent chaining
- Better error handling
- Agent-specific optimizations

### 💰 Budget Management
- Cost estimation
- Spending alerts
- Cost optimization strategies
- Invoice generation

### 📊 API & Server
- WebSocket support
- Batch processing API
- Advanced analytics
- Authentication/authorization

### 📚 Documentation
- Translate to other languages
- Add more examples
- Tutorial videos
- API documentation

### 🧪 Testing
- Unit tests
- Integration tests
- Performance tests
- Security tests

---

## Pull Request Process

### Before Submitting

1. **Ensure code quality:**
   ```bash
   black src/
   flake8 src/
   pytest tests/
   ```

2. **Update documentation:**
   - Update relevant `.md` files
   - Add docstrings to new functions
   - Update API documentation

3. **Test your changes:**
   ```bash
   python main.py --mode interactive
   # Test manually with different providers
   ```

### Submitting PR

1. Push to your fork
2. Create Pull Request with:
   - Clear title (e.g., "Add Google Cloud Speech integration")
   - Description of changes
   - Related issues (if any)
   - Testing instructions

**PR Template:**
```markdown
## Description
Brief description of what this PR does

## Related Issues
Closes #issue_number

## Changes
- Change 1
- Change 2

## Testing
How to test these changes:
```

### Review Process

- At least 1 approval required
- All checks must pass
- No merge conflicts
- Coverage should not decrease

---

## Development Setup

### Project Structure
```
src/
├── audio/           # Audio processing
├── transcription/   # STT implementations
├── agents/          # AI agent integrations
├── api/             # FastAPI server
├── core/            # Main pipeline
└── budget/          # Cost tracking

tests/
├── test_audio.py
├── test_transcription.py
├── test_agents.py
└── test_budget.py

config/
└── config.yaml      # Configuration

docs/
├── README.md
├── EXAMPLES.md
└── CONTRIBUTING.md
```

### Adding a New Feature

**Example: Add new transcriber provider**

1. Create new file: `src/transcription/my_provider.py`
   ```python
   from .transcriber import Transcriber
   
   class MyProviderTranscriber(Transcriber):
       def transcribe(self, audio_path: str) -> str:
           # Implementation
           pass
   ```

2. Register in factory: `src/transcription/smart_factory.py`
   ```python
   from .my_provider import MyProviderTranscriber
   
   _transcribers = {
       ...
       "my_provider": MyProviderTranscriber,
   }
   ```

3. Add tests: `tests/test_my_provider.py`
   ```python
   def test_my_provider_transcription():
       # Test implementation
       pass
   ```

4. Update docs: `EXAMPLES.md`

5. Submit PR!

---

## Bug Reports

### Report Format

**Title:** Brief description of bug

**Description:**
```markdown
## Environment
- OS: Linux/Windows/macOS
- Python: 3.9/3.10/3.11
- Provider: openai/vosk/etc

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Logs
```
error logs here
```

## Screenshots
(if applicable)
```

---

## Feature Requests

### Request Format

**Title:** Brief description

**Description:**
```markdown
## Problem
What problem does this solve?

## Proposed Solution
How should this work?

## Benefits
Why is this useful?

## Alternatives
Are there other ways to solve this?
```

---

## Code Review Guidelines

### For Authors
- Keep PRs focused and small
- Add tests for new features
- Update documentation
- Respond to feedback promptly

### For Reviewers
- Be respectful and constructive
- Suggest improvements with examples
- Approve when satisfied
- Request changes clearly

---

## Performance Guidelines

### Optimization Tips
- Cache transcription results
- Use free providers first
- Batch process when possible
- Monitor memory usage

### Performance Testing
```bash
python -m pytest tests/ --benchmark
```

---

## Security Guidelines

- Never commit API keys
- Always use `.env` for secrets
- Validate user input
- Use HTTPS in production
- Report security issues privately

**Report Security Issues:**
Email: security@example.com (Don't post publicly)

---

## Documentation Standards

### Code Comments
```python
def smart_provider_selection(duration: float) -> str:
    """
    Smart selection of transcription provider based on budget.
    
    Args:
        duration: Audio duration in seconds
    
    Returns:
        Provider name (e.g., "openai", "vosk")
    
    Raises:
        ValueError: If no providers available
    
    Examples:
        >>> select_provider(60)
        'openai'
    """
```

### Docstring Format
Use Google-style docstrings:
```python
def function(arg1: str, arg2: int) -> bool:
    """Short description.
    
    Longer description if needed.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When this happens
    
    Examples:
        >>> function("test", 1)
        True
    """
```

---

## Useful Resources

- [Python Style Guide (PEP 8)](https://pep8.org)
- [Git Workflow](https://git-scm.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Testing with Pytest](https://pytest.org)

---

## Community

- **Issues:** Report bugs and request features
- **Discussions:** Ask questions and share ideas
- **Pull Requests:** Contribute code
- **Wiki:** Community knowledge base

---

## License

By contributing, you agree that your contributions will be licensed under MIT License.

---

## Recognition

Contributors will be recognized in:
- `CONTRIBUTORS.md`
- Release notes
- GitHub contributors page

---

Thank you for contributing! 🙏

Créé avec ❤️ par la communauté  
Dernière mise à jour: 2026-08-25
````
