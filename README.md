# Pyragogy Handbook n8n Workflow

> **Elevating Collaborative Intelligence**
> The orchestration engine behind the AI-powered Pyragogy Handbook.


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![n8n Version](https://img.shields.io/badge/n8n-1.0%2B-blue.svg)](https://n8n.io/)
[![Language](https://img.shields.io/badge/lang-Markdown-blue.svg)](#)

---

## 🧠 Overview

This repository contains the core **n8n automation workflow** that powers the AI-driven co-authoring process of the **Pyragogy Handbook**. It is a modular, scalable, and open-source system designed to orchestrate multiple AI agents—alongside human contributors—to collaboratively draft, refine, validate, and persist high-quality Markdown-based knowledge.

> As a cornerstone of [Pyragogy.org](https://pyragogy.org), this workflow exemplifies a new paradigm for AI-human co-creation in the context of peer learning.

---

## 🎯 Purpose

The `pyragogy-handbook-n8n-workflow` transforms complexity into clarity by automating:

* Distributed writing tasks across AI agents
* Quality control and review cycles
* Semantic metadata management
* Multi-channel persistence and collaboration

---

## ✨ Key Features

* **Multi-Agent Orchestration**
  Coordinate specialized agents (e.g., Summarizer, Synthesizer, QA Agent) via a single automated workflow.

* **Automated Markdown Generation**
  Draft and refine handbook sections dynamically from human prompts or AI insights.

* **Cognitive Feedback Loops**
  Integrate human and AI feedback phases to ensure accuracy and depth.

* **Versioning & Storage**
  Syncs with GitHub (for version control) and PostgreSQL/Supabase (for structured storage and queryability).

* **Composable & Extensible**
  Built on n8n—easily adaptable to your own agents, triggers, and integrations.

---
## 🧬 Architecture

```mermaid
graph TD
    A[Webhook Trigger] --> B[Meta-Orchestrator]
    B --> C[Summarizer]
    C --> D[Synthesizer]
    D --> E[Peer Reviewer]
    E --> F[Sensemaking Agent]
    F --> G[Prompt Engineer]
    G --> H[Consensus Check]
    H -- Major Issue --> D
    H -- OK --> I[Add Metadata + Review Content]
    I --> J[Human Approval Email]
    J --> K{Human Decision}
    K -- Approved --> L[PostgreSQL + GitHub Commit]
    K -- Rejected --> M[Loop Feedback or Log Rejection]

## 🚀 Getting Started

### Requirements

* A running **n8n** instance (self-hosted or via cloud)
* API access to LLMs (e.g., OpenAI, Anthropic, etc.)
* A **GitHub** repo for storing content
* A **PostgreSQL** database (Supabase optional)

---

### Installation

```bash
git clone https://github.com/pyragogy/pyragogy-handbook-n8n-workflow.git
cd pyragogy-handbook-n8n-workflow
```

1. Import the workflow into your n8n instance
   → Go to **Workflows > Import from File**
   → Choose `workflow.json` from this repo

2. Configure credentials for:

   * OpenAI or other LLM providers
   * GitHub (with write access token)
   * PostgreSQL/Supabase (connection string)

3. Adjust environment variables, repo names, and database config inside workflow nodes.

---

## 🛠️ Usage

Once configured, you can:

* Trigger the workflow manually or via webhook/scheduler
* Send a content idea or update
* Let agents generate, synthesize, validate, and persist the content
* Review/edit final output on GitHub
* Analyze metadata or query it from your PostgreSQL/Supabase backend

---

## 🌐 External Resources

* 🔗 [Pyragogy.org](https://pyragogy.org) – The ecosystem behind the vision
* 📘 [n8n Docs](https://docs.n8n.io) – Workflow orchestration platform
* 📜 *Pyragogy Manifesto* – Coming soon
* 📚 *Live Handbook Output* – Coming soon

---

## 🤝 Contributing

We welcome contributions from:

* Researchers
* Technical writers
* LLM & n8n developers
* Workflow automation geeks

**Get Involved:**

* 🐛 Report bugs via [GitHub Issues](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/issues)
* 💡 Suggest features or agent roles
* 📦 Submit pull requests with fixes or new modules

Read our [Contributing Guidelines](CONTRIBUTING.md) (coming soon).

---

## ❤️ Acknowledgements

Made with ♥ by [Pyragogy.ai](https://pyragogy.org)
Building bridges between cognition, automation, and peer learning.

