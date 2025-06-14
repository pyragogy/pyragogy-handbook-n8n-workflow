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

The workflow leverages **n8n** as its orchestration layer, connecting various services and AI models.

```mermaid
graph TD
    A[Webhook Trigger] --> B[Meta-Orchestrator]
    B --> C[Summarizer]
    C --> D[Synthesizer]
    D --> E[Peer Reviewer]
    E --> F[Sensemaking Agent]
    F --> G[Prompt Engineer]
    G --> H[Consensus Check]
    H --> |Major Issue| D
    H --> |OK| I[Add Metadata + Review Content]
    I --> J[Human Approval Email]
    J --> K{Human Decision}
    K --> |Approved| L[PostgreSQL + GitHub Commit]
    K --> |Rejected| M[Loop Feedback or Log Rejection]
```

### Agent Roles

* **Meta-Orchestrator**: Coordinates the entire workflow and manages task distribution
* **Summarizer**: Extracts key insights and creates concise summaries
* **Synthesizer**: Combines multiple sources into coherent content
* **Peer Reviewer**: Validates content quality and consistency
* **Sensemaking Agent**: Analyzes deeper patterns and connections
* **Prompt Engineer**: Optimizes interactions between agents

---

## 🚀 Getting Started

### Prerequisites

* A running **n8n** instance (self-hosted or cloud)
* API access to LLMs (OpenAI, Anthropic, etc.)
* A **GitHub** repository for content storage
* A **PostgreSQL** database (Supabase recommended)
* Node.js 16+ (for local development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pyragogy/pyragogy-handbook-n8n-workflow.git
   cd pyragogy-handbook-n8n-workflow
   ```

2. **Import workflow into n8n**
   * Navigate to **Workflows > Import from File**
   * Select `workflow.json` from this repository
   * Activate the imported workflow

3. **Configure credentials**
   
   Set up the following credentials in your n8n instance:
   
   * **OpenAI/LLM Provider**: API key for language model access
   * **GitHub**: Personal access token with repository write permissions
   * **PostgreSQL/Supabase**: Database connection string
   * **SMTP**: Email configuration for approval notifications

4. **Environment Configuration**
   
   Update the following variables in workflow nodes:
   ```json
   {
     "GITHUB_REPO": "your-username/your-handbook-repo",
     "DATABASE_URL": "postgresql://user:pass@host:port/dbname",
     "NOTIFICATION_EMAIL": "approver@your-domain.com"
   }
   ```

### Database Setup

Execute the following SQL to create required tables:

```sql
CREATE TABLE handbook_content (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    metadata JSONB,
    status VARCHAR(50) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_handbook_status ON handbook_content(status);
CREATE INDEX idx_handbook_metadata ON handbook_content USING GIN(metadata);
```

---

## 🛠️ Usage

### Manual Trigger

1. Navigate to your n8n workflow
2. Click "Execute Workflow"
3. Provide input parameters:
   ```json
   {
     "topic": "AI Ethics in Education",
     "context": "Exploring ethical implications...",
     "priority": "high"
   }
   ```

### Webhook Trigger

Send a POST request to your workflow webhook:

```bash
curl -X POST "https://your-n8n-instance.com/webhook/pyragogy-handbook" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Collaborative Learning Patterns",
    "context": "Analysis of peer-to-peer learning dynamics"
  }'
```

### Scheduled Execution

Configure a cron trigger in n8n to run the workflow periodically:
* Daily content updates: `0 9 * * *`
* Weekly reviews: `0 10 * * 1`

---

## 📊 Monitoring & Analytics

The workflow includes built-in monitoring capabilities:

* **Execution Metrics**: Track success rates and processing times
* **Content Quality Scores**: AI-generated quality assessments
* **Human Feedback**: Approval/rejection rates and comments
* **Error Handling**: Comprehensive logging and retry mechanisms

Access metrics through:
* n8n execution history
* PostgreSQL analytics queries
* Custom dashboard (coming soon)

---

## 🔧 Customization

### Adding New Agents

1. Create a new HTTP node in n8n
2. Configure the agent's specific prompt and parameters
3. Connect it to the workflow at the appropriate stage
4. Update the consensus check logic if needed

### Modifying Content Structure

Edit the content template in the Synthesizer node:

```javascript
const contentTemplate = {
  title: "{{ $json.title }}",
  sections: [
    { heading: "Overview", content: "{{ $json.overview }}" },
    { heading: "Key Concepts", content: "{{ $json.concepts }}" },
    { heading: "Applications", content: "{{ $json.applications }}" }
  ],
  metadata: {
    tags: "{{ $json.tags }}",
    difficulty: "{{ $json.difficulty }}",
    estimated_reading_time: "{{ $json.reading_time }}"
  }
};
```

---

## 🌐 Integration Ecosystem

### Compatible Services

* **AI Providers**: OpenAI GPT-4, Anthropic Claude, Google Gemini
* **Version Control**: GitHub, GitLab, Bitbucket
* **Databases**: PostgreSQL, Supabase, MongoDB
* **Notification**: Email (SMTP), Slack, Discord, Microsoft Teams
* **Storage**: AWS S3, Google Cloud Storage, Azure Blob

### API Endpoints

The workflow exposes several endpoints for integration:

* `POST /webhook/pyragogy-handbook` - Trigger content creation
* `GET /api/content/{id}` - Retrieve specific content
* `POST /api/feedback` - Submit human feedback
* `GET /api/metrics` - Access workflow analytics

---

## 🧪 Testing

### Unit Tests

Run individual node tests:
```bash
npm test -- --testPathPattern=nodes
```

### Integration Tests

Test the complete workflow:
```bash
npm run test:integration
```

### Load Testing

Simulate concurrent requests:
```bash
npm run load-test -- --concurrent=10 --duration=60s
```

---

## 🔐 Security Considerations

* **API Keys**: Store all credentials securely in n8n's credential system
* **Webhook Security**: Use webhook authentication tokens
* **Database Access**: Implement role-based access control
* **Content Validation**: Sanitize all user inputs and AI outputs
* **Audit Logging**: Track all content modifications and approvals

---

## 📈 Performance Optimization

### Recommended Settings

* **Workflow Timeout**: 300 seconds for complex content generation
* **Concurrent Executions**: Limit to 3 to prevent API rate limiting
* **Retry Logic**: 3 attempts with exponential backoff
* **Memory Usage**: Monitor for large content processing

### Scaling Guidelines

* **Horizontal Scaling**: Deploy multiple n8n instances with load balancing
* **Database Optimization**: Use connection pooling and read replicas
* **Caching**: Implement Redis for frequently accessed content
* **CDN Integration**: Serve static assets through CloudFront or similar

---

## 🤝 Contributing

We welcome contributions from the community! Here's how to get involved:

### Areas of Interest

* **AI Agent Development**: Create specialized agents for specific domains
* **Workflow Optimization**: Improve processing efficiency and reliability
* **Documentation**: Enhance guides and examples
* **Testing**: Expand test coverage and scenarios
* **Integrations**: Add support for new services and platforms

### Contribution Process

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Install dependencies
npm install

# Start development environment
npm run dev

# Run tests
npm test

# Lint code
npm run lint
```

---

## 📚 Resources & Documentation

### Essential Reading

* 📖 [n8n Documentation](https://docs.n8n.io) - Comprehensive workflow automation guide
* 🧠 [AI Agent Design Patterns](https://pyragogy.org/patterns) - Best practices for multi-agent systems
* 🔄 [Workflow Optimization Guide](https://pyragogy.org/optimization) - Performance tuning strategies

### Community

* 💬 [Discord Server](https://discord.gg/pyragogy) - Real-time community discussions
* 📧 [Mailing List](https://groups.google.com/g/pyragogy) - Monthly updates and announcements
* 🐦 [Twitter](https://twitter.com/pyragogy) - Latest news and insights

### Support

* 🐛 [GitHub Issues](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/issues) - Bug reports and feature requests
* 📖 [Wiki](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/wiki) - Extended documentation and tutorials
* 💡 [Discussions](https://github.com/pyragogy/pyragogy-handbook-n8n-workflow/discussions) - Community Q&A

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

### Core Team

* **Project Lead**: [Fabrizio Terzi] - Vision and architecture
* **Technical Lead**: [Name] - n8n workflow development
* **AI Specialist**: [Name] - Agent design and optimization
* **Community Manager**: [Name] - Documentation and support

### Special Thanks

* The **n8n community** for their excellent automation platform
* **OpenAI** and **Anthropic** for providing powerful language models
* The **Pyragogy community** for continuous feedback and contributions
* All **beta testers** who helped refine the workflow

---

<div align="center">

**Made with ♥ by the [Pyragogy.org](https://pyragogy.org) community**

*Building bridges between cognition, automation, and peer learning*

[![Pyragogy](https://img.shields.io/badge/Powered%20by-Pyragogy-brightgreen.svg)](https://pyragogy.org)

</div>
