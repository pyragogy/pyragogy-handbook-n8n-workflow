# Pyragogy Handbook n8n Workflow

[![CI Status](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/workflows/test/badge.svg)](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Version](https://img.shields.io/badge/n8n-1.0%2B-blue.svg)](https://n8n.io/)
[![English](https://img.shields.io/badge/Language-EN-blue.svg)](README.en.md)
[![Italiano](https://img.shields.io/badge/Lingua-IT-blue.svg)](README.it.md)

An advanced co-authoring workflow powered by n8n that leverages specialized AI agents and Human-in-the-Loop mechanisms for collaborative generation of the Pyragogy Handbook.

## 🌟 Key Features

* **🤖 Multi-Agent Orchestration**: Seven specialized AI agents working in synergy
* **👥 Human-in-the-Loop**: Integrated human review to ensure content quality
* **🔄 Iterative Improvement**: Automatic revision cycles
* **📊 Advanced Monitoring**: Grafana dashboards and Prometheus metrics
* **🧪 Automated Tests**: Full test suite for CI/CD
* **🎨 Simplified UI**: Web interface for user-friendly input
* **📈 Observability**: Comprehensive logging, metrics, and alerting

## 🚀 Quick Start

### Prerequisites

* Docker and Docker Compose
* Git
* (Optional) Python 3.7+ for local testing

### Fast Installation

```bash
# Clone the repository
git clone https://github.com/pyragogy/pyragogy-handbook-n8n-workflow.git
cd pyragogy-handbook-n8n-workflow

# Copy and configure environment variables
cp .env.template .env
# Edit .env with your credentials

# Start all services
docker-compose -f scripts/docker-compose-monitoring.yml up -d

# Import the workflow into n8n
curl -X POST http://localhost:5678/rest/workflows \
  -H "Content-Type: application/json" \
  -d @workflow/pyragogy_master_workflow.json
```

### Access Services

* **n8n**: [http://localhost:5678](http://localhost:5678) (admin/password)
* **Grafana**: [http://localhost:3000](http://localhost:3000) (admin/admin)
* **Prometheus**: [http://localhost:9090](http://localhost:9090)
* **Input Interface**: Open `ui/simple-input-interface.html` in your browser

## 📚 Documentation

### Main Docs

* [**README Italiano**](README.it.md): Full documentation in Italian
* [**Architecture Notes**](docs/architecture-notes.md): Technical details of the architecture
* [**Improved Documentation**](docs/improved_documentation.md): Workflow structure deep-dive, output examples, and agent role breakdown

### Specific Guides

* [**Automated Testing**](tests/README.md): How to run and extend tests
* [**Monitoring**](monitoring/README.md): Setup and use of the monitoring system
* [**User Interface**](ui/README.md): How to use the simplified web interface

### Visuals

* [**Architecture Diagram**](docs/images/workflow_architecture_diagram.png): Overview of full architecture
* [**n8n Mockup**](docs/images/n8n_workflow_mockup.png): Visualization of the n8n interface
* [**Agent Flow**](docs/images/agent_flow_diagram.png): Agent orchestration diagram
* [**Monitoring Dashboard**](docs/images/monitoring_dashboard_mockup.png): Sample Grafana dashboard

## 🏗️ Architecture

The workflow is organized into the following layers:

1. **Input Layer**: Webhook trigger to receive requests
2. **Orchestration Layer**: Meta-Orchestrator for dynamic planning
3. **Agent Layer**: Seven specialized AI agents
4. **Consensus Layer**: Quality consensus mechanism
5. **HITL Layer**: Human review via email/webhook
6. **Storage Layer**: PostgreSQL and GitHub for persistence
7. **Monitoring Layer**: Prometheus, Grafana, and alerting

### Specialized AI Agents

* **Summarizer**: Condenses long texts into key points
* **Synthesizer**: Generates new content from ideas and input
* **Peer Reviewer**: Analyzes and critiques content
* **Sensemaking**: Connects content to existing context
* **Prompt Engineer**: Optimizes prompts for other agents
* **Onboarding/Explainer**: Provides guidance and onboarding
* **Archivist**: Handles storage, versioning, and metadata

## 🧪 Testing and Quality

### Running Tests

```bash
# Automated tests
cd tests
python test_workflow.py

# Test with custom URL
python test_workflow.py http://your-n8n-instance:5678
```

### CI/CD

The workflow includes GitHub Actions for:

* Automated tests on push/PR
* Workflow JSON validation
* Documentation checks
* Auto-deploy (configurable)

## 📊 Monitoring

### Available Metrics

* Workflow executions (success/failure)
* Agent performance (time, tokens, cost)
* Human reviews (pending, response time)
* System resources (CPU, memory, disk)
* Error rate and latency

### Grafana Dashboards

Preconfigured dashboards for:

* General system overview
* Workflow performance
* Token/cost analysis
* Resource monitoring
* Error management

## 🎨 User Interface

The simplified web interface (`ui/simple-input-interface.html`) allows you to:

* Submit new ideas to the workflow without JSON
* Configure metadata (tags, phase, rhythm)
* Monitor submission status
* Manage human review toggle

## 🔧 Advanced Configuration

### Main Environment Variables

```bash
# Database
POSTGRES_HOST=localhost
POSTGRES_DB=pyragogy
POSTGRES_USER=pyragogy
POSTGRES_PASSWORD=your_password

# OpenAI
OPENAI_API_KEY=your_openai_key

# GitHub
GITHUB_TOKEN=your_github_token
GITHUB_REPO=your_username/your_repo

# Email (for HITL)
EMAIL_HOST=smtp.gmail.com
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# n8n
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your_password
```

### Agent Customization

Agents can be customized by editing the prompts in the OpenAI nodes of the n8n workflow. Each agent has:

* A system prompt tailored to its role
* Configurable temperature and max\_tokens
* Retry and fallback logic

## 🤝 Contributing

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines

* Follow existing code conventions
* Add tests for new features
* Update documentation
* Test locally before committing

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

* **n8n Team**: For the amazing automation platform
* **OpenAI**: For the GPT models powering the agents
* **Pyragogy Community**: For the inspiration and feedback
* **Contributors**: Everyone who contributed to the project

## 📞 Support

* **Issues**: [GitHub Issues](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/issues)
* **Discussions**: [GitHub Discussions](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/discussions)
* **Email**: [info@pyragogy.org](mailto:info@pyragogy.org)

---

**Note**: This is an evolving project. Feedback and contributions are always welcome!
