# Changelog

All significant changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## \[2.0.0] - 2024-12-06

### Added

* **Simplified User Interface**: New web UI (`ui/simple-input-interface.html`) to submit input to the workflow without manually constructing JSON
* **Automated Tests**: Complete test suite (`tests/test_workflow.py`) to validate workflow functionality
* **Advanced Monitoring System**:

  * Prometheus configuration for metrics collection
  * Preconfigured Grafana dashboards
  * Custom monitoring script (`monitoring/monitor.py`)
  * Alert rules for critical situations
* **CI/CD Pipeline**: GitHub Actions for automated tests and validation
* **Improved Documentation**:

  * Detailed guide with flow diagrams
  * Workflow output examples
  * In-depth descriptions of agent roles
* **Visualizations**:

  * Workflow architecture diagram
  * n8n interface mockup
  * AI agent flow diagram
  * Grafana monitoring dashboard
* **Advanced Docker Compose**: Configuration with integrated monitoring services
* **Improved Database Schema**: Tables for metrics, error logging, and performance tracking

### Changed

* **README**: Completely rewritten with detailed information about all new features
* **Repository Structure**: Improved organization with dedicated directories for tests, monitoring, and UI
* **Documentation**: Added component-specific documentation
* **Error Handling**: Structured logging and improved retry mechanisms

### Technical

* Added support for custom Prometheus metrics
* Implemented alerting system with configurable rules
* Created database initialization script with full schema
* Added support for integration and payload validation tests

## \[1.0.0] - 2024-01-15

### Added

* Initial implementation of multi-agent n8n workflow
* Meta-Orchestrator for dynamic agent orchestration
* Seven specialized AI agents:

  * Summarizer Agent
  * Synthesizer Agent
  * Peer Reviewer Agent
  * Sensemaking Agent
  * Prompt Engineer Agent
  * Onboarding/Explainer Agent
  * Archivist Agent
* Human-in-the-Loop (HITL) mechanism with email notifications
* PostgreSQL integration for data persistence
* GitHub integration for content versioning
* Consensus mechanism with iterative cycles
* Basic documentation in Italian and English
* Docker Compose for local deployment
* Configuration template (.env.template)

### Initial Features

* Webhook trigger for external input
* Automated GitHub conflict handling
* YAML front-matter metadata for generated content
* Dynamic agent routing system
* Basic operational logging

---

## Release Format

Releases follow the `vYYYY.MM.DD` format for major releases and `vYYYY.MM.DD.patch` for hotfixes.

## Contributing to the Changelog

When contributing to the project:

1. Add your changes to the "Unreleased" section
2. Use the categories: Added, Changed, Deprecated, Removed, Fixed, Security
3. Include references to issues/PRs when applicable
4. Keep the format consistent
