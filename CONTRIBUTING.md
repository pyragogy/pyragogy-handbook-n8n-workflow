# Contribution Guide

Thank you for your interest in contributing to the Pyragogy Handbook n8n Workflow! This guide will help you get started.

## 🤝 How to Contribute

### Types of Contributions Welcome

* **🐛 Bug Reports**: Report issues or unexpected behavior
* **💡 Feature Requests**: Suggest new features or improvements
* **📝 Documentation**: Improve or expand the documentation
* **🔧 Code**: Implement new features or fix bugs
* **🧪 Tests**: Add or enhance automated tests
* **🎨 UI/UX**: Improve user interface or user experience

### Before You Start

1. **Check Existing Issues**: See if your problem or idea has already been discussed
2. **Read the Documentation**: Get familiar with the workflow architecture and behavior
3. **Set Up the Environment**: Follow the setup guide in the README

## 🚀 Development Environment Setup

### Prerequisites

* Docker and Docker Compose
* Git
* Python 3.7+ (for tests)
* Node.js 16+ (optional, for UI development)

### Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/pyragogy-handbook-n8n-workflow.git
cd pyragogy-handbook-n8n-workflow

# 2. Configure upstream remote
git remote add upstream https://github.com/pyragogy/pyragogy-handbook-n8n-workflow.git

# 3. Create a branch for your feature
git checkout -b feature/your-feature-name

# 4. Configure environment
cp .env.template .env
# Edit .env with your test credentials

# 5. Start development services
docker-compose -f scripts/docker-compose-monitoring.yml up -d

# 6. Install test dependencies
pip install -r tests/requirements.txt
```

## 📝 Contribution Process

### 1. Planning

* **For Bugs**: Create an issue describing the problem, steps to reproduce, and expected behavior
* **For Features**: Create an issue outlining the feature, use case, and benefits
* **Discuss**: Join the issue discussion before starting work

### 2. Development

```bash
# Keep your fork up to date
git fetch upstream
git checkout main
git merge upstream/main

# Create a new branch
git checkout -b feature/your-feature-name

# Develop your feature
# ... make your changes ...

# Test your changes
cd tests
python test_workflow.py

# Commit with descriptive messages
git add .
git commit -m "feat: add new feature X"
```

### 3. Testing

Before submitting a PR, ensure:

* [ ] All existing tests pass
* [ ] You’ve added tests for new features
* [ ] The n8n workflow runs correctly
* [ ] Documentation is up-to-date

```bash
# Run all tests
python tests/test_workflow.py

# Validate workflow JSON
python -m json.tool workflow/pyragogy_master_workflow.json > /dev/null

# Check documentation
# Ensure all links work
```

### 4. Pull Request

1. **Push your branch**:

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create PR**: Go to GitHub and open a Pull Request

3. **PR Template**: Use the provided template and include:

   * Clear description of the changes
   * Reference to related issues
   * Screenshots for UI changes
   * Notes for reviewers

## 📋 Code Standards

### General Conventions

* **Language**: Comments and docs in Italian, code in English
* **Format**: Use consistent formatting
* **Names**: Use descriptive variable and function names

### n8n Workflow

* **Nodes**: Use descriptive names for nodes
* **Comments**: Add notes for complex nodes
* **Organization**: Keep layout clean and logical
* **Versioning**: Increment workflow version for significant changes

### Python (Tests and Scripts)

```python
# Use docstrings for functions
def test_workflow_execution():
    """Test basic execution of the workflow."""
    pass

# Handle exceptions properly
try:
    result = api_call()
except Exception as e:
    logger.error(f"API Error: {e}")
    return False
```

### JavaScript (n8n Function Nodes)

```javascript
// Use comments to explain logic
// Prepare data for the Synthesizer agent
const agentInput = {
  role: "synthesizer",
  content: $json.input,
  context: $json.context || {}
};

return { json: agentInput };
```

## 🧪 Test Guidelines

### Workflow Tests

* **Coverage**: Test all major paths
* **Isolation**: Each test should be independent
* **Data**: Use realistic but non-sensitive test data
* **Cleanup**: Clean test data after execution

### Adding New Tests

```python
def test_new_feature(self) -> bool:
    """Test the new feature."""
    try:
        # Setup
        test_data = {"key": "value"}

        # Execution
        result = call_new_feature(test_data)

        # Verification
        if result.status == "success":
            self.log_test("New Feature", True, "Works correctly")
            return True
        else:
            self.log_test("New Feature", False, f"Error: {result.error}")
            return False

    except Exception as e:
        self.log_test("New Feature", False, f"Exception: {str(e)}")
        return False
```

## 📚 Documentation

### Updating Documentation

* **README**: Update for major new features
* **Docs**: Create specific files for complex features
* **Comments**: Keep code comments updated
* **Changelog**: Add changes to CHANGELOG.md

### Documentation Style

* **Clarity**: Write for users of various technical levels
* **Examples**: Include practical examples and use cases
* **Structure**: Use headings and lists to organize
* **Images**: Add screenshots or diagrams when useful

## 🔍 Review Process

### What to Expect

1. **Automatic Review**: GitHub Actions will run automated tests
2. **Manual Review**: A maintainer will review your code
3. **Feedback**: You may receive change requests
4. **Merge**: After approval, your PR will be merged

### Review Criteria

* **Functionality**: Does the code do what it should?
* **Quality**: Is the code clean and well-structured?
* **Tests**: Are there adequate tests?
* **Documentation**: Is it up-to-date and clear?
* **Compatibility**: Does it avoid breaking existing features?

## 🏷️ Commit Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

### Types

* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Formatting, missing semicolons, etc.
* `refactor`: Code refactoring
* `test`: Adding or updating tests
* `chore`: Build/dependencies/infra changes

### Examples

```bash
feat(agents): add new Translator agent
fix(webhook): fix timeout error handling
docs(readme): update installation instructions
test(workflow): add test for agent orchestration
```

## 🆘 Getting Help

### Support Channels

* **GitHub Issues**: For bugs and feature requests
* **GitHub Discussions**: For general questions and discussions
* **Email**: [pyragogy@example.com](mailto:pyragogy@example.com) for private matters

### Before Asking for Help

1. Check existing documentation
2. Search closed issues
3. Verify your environment is correctly configured
4. Try reproducing the problem with test data

### Provide Useful Info

When asking for help, include:

* Software versions (n8n, Docker, Python)
* Operating system
* Steps to reproduce the problem
* Full error logs
* Configuration (without sensitive credentials)

## 🎉 Acknowledgments

All contributors will be credited in the README and release notes. Contributing to this project means:

* Being part of an innovative community
* Learning cutting-edge technologies (AI, automation, n8n)
* Supporting a meaningful open-source project
* Gaining skills in distributed systems and AI

## 📄 License

By contributing to this project, you agree that your contributions will be released under the project's MIT license.

---

**Thank you for your contribution! 🙏**

Every contribution, big or small, is valuable to the Pyragogy community.
