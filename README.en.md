# Pyragogy n8n Co-Authoring Workflow

[![CI Status](https://img.shields.io/badge/CI-passing-brightgreen.svg)](https://github.com/pyragogy/pyragogy-n8n-workflow/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](https://img.shields.io/badge/Language-EN-blue.svg)](README.en.md)
[![Italiano](https://img.shields.io/badge/Lingua-IT-blue.svg)](README.it.md)

## 📖 Project Overview

The Pyragogy n8n Co-Authoring Workflow is an advanced multi-agent automation
system designed to autonomously compile the Pyragogy Handbook. It leverages
GPT-class Large Language Models (LLMs) for content generation and a
"Human-in-the-Loop" (HITL) mechanism to ensure quality and accuracy.

### Key Features:

* **Multi-Agent Orchestration**: Utilizes a Meta-Orchestrator to dynamically
    sequence specialized AI agents (Summarizer, Synthesizer, Peer Reviewer,
    Sensemaking Agent, Prompt Engineer, Onboarding Agent, Archivist).
* **Human-in-the-Loop (HITL)**: Critical content proposals (e.g., Handbook
    entries) undergo human review via secure webhooks (email, Slack, or
    Telegram Actions).
* **Consensus Mechanism**: A "Peer Review Board" of AI agents evaluates
    content, triggering redrafting loops based on a majority vote to resolve
    major issues.
* **Persistent Storage**: Content and metadata are stored in a Postgres
    database.
* **Versioned Archiving**: Approved Handbook entries are committed to a GitHub
    repository with unique, timestamped file versions and YAML front-matter.
* **Bilingual Documentation**: Comprehensive guides available in both Italian
    and English.

## 🚀 Quick Start (Docker)

To get a local instance of the Pyragogy n8n Co-Authoring Workflow up and
running quickly, follow these steps:

1.  **Prerequisites**: Ensure you have Docker and Docker Compose installed.
2.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/pyragogy/pyragogy-n8n-workflow.git](https://github.com/pyragogy/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```
3.  **Configure Environment Variables**:
    Copy the template file and fill in your details, especially your OpenAI
    API key and GitHub Personal Access Token (PAT).
    ```bash
    cp .env.template .env
    # Open .env in your preferred editor and fill in the values
    ```
4.  **Start Services**:
    This command will spin up n8n, Postgres, and Redis containers.
    ```bash
    docker-compose -f scripts/docker-compose.yml up -d
    ```
5.  **Access n8n**:
    Once the containers are running, access the n8n UI, typically at
    `http://localhost:5678`.
6.  **Import Workflow**:
    Import the `workflow/pyragogy_master_workflow.json` file into your n8n
    instance. Remember to activate the workflow.

For more detailed setup instructions, refer to `docs/setup-quickstart.md`.

## 📚 Documentation

* [**Architecture Notes**](docs/architecture-notes.md): Deep dive into the
    system's design, agent roles, and interaction mechanisms.
* [**Setup & Quickstart Guide**](docs/setup-quickstart.md): Detailed steps
    to install and run the workflow.
* [**Contributing Guidelines**](CONTRIBUTING.md): How to contribute to this
    project.

## 🤝 Contribution

We welcome contributions from developers, AI enthusiasts, content strategists,
and anyone interested in autonomous content generation. Please see
`CONTRIBUTING.md` for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.

## Versioning

Releases are tagged using the format `vYYYY.MM.DD`. Handbook entries generated
by the workflow are versioned as `chapter_slug_vTIMESTAMP.md`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes.

---
