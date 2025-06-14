# Workflow di Co-Authoring n8n di Pyragogy

[![Stato CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](https://github.com/pyragogy/pyragogy-n8n-workflow/actions)
[![Licenza: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](https://img.shields.io/badge/Language-EN-blue.svg)](README.en.md)
[![Italiano](https://img.shields.io/badge/Lingua-IT-blue.svg)](README.it.md)

## 📖 Panoramica del Progetto

Il Workflow di Co-Authoring n8n di Pyragogy è un sistema avanzato di
automazione multi-agente progettato per compilare autonomamente l'Handbook di
Pyragogy. Sfrutta i Large Language Models (LLM) di classe GPT per la
generazione di contenuti e un meccanismo "Human-in-the-Loop" (HITL) per
garantire qualità e accuratezza.

### Caratteristiche Principali:

* **Orchestrazione Multi-Agente**: Utilizza un Meta-Orchestrator per
    sequenziare dinamicamente agenti AI specializzati (Summarizer, Synthesizer,
    Peer Reviewer, Sensemaking Agent, Prompt Engineer, Onboarding Agent, Archivista).
* **Human-in-the-Loop (HITL)**: Le proposte di contenuto critiche (es. voci
    dell'Handbook) sono sottoposte a revisione umana tramite webhook sicuri
    (email, Slack o Telegram Actions).
* **Meccanismo di Consenso**: Una "Commissione di Revisione Paritaria" di
    agenti AI valuta il contenuto, attivando cicli di rielaborazione basati
    su un voto a maggioranza per risolvere problemi importanti.
* **Archiviazione Persistente**: Contenuti e metadati sono memorizzati in
    un database Postgres.
* **Archiviazione Versionata**: Le voci dell'Handbook approvate vengono
    commesse in un repository GitHub con versioni di file uniche e con
    timestamp e YAML front-matter.
* **Documentazione Bilingue**: Guide complete disponibili sia in italiano
    che in inglese.

## 🚀 Guida Rapida (Docker)

Per avviare rapidamente un'istanza locale del Workflow di Co-Authoring n8n di
Pyragogy, segui questi passaggi:

1.  **Prerequisiti**: Assicurati di avere Docker e Docker Compose installati.
2.  **Clona il Repository**:
    ```bash
    git clone [https://github.com/pyragogy/pyragogy-n8n-workflow.git](https://github.com/pyragogy/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```
3.  **Configura le Variabili d'Ambiente**:
    Copia il file template e inserisci i tuoi dettagli, in particolare la tua
    chiave API OpenAI e il Personal Access Token (PAT) di GitHub.
    ```bash
    cp .env.template .env
    # Apri .env nel tuo editor preferito e inserisci i valori
    ```
4.  **Avvia i Servizi**:
    Questo comando avvierà i container di n8n, Postgres e Redis.
    ```bash
    docker-compose -f scripts/docker-compose.yml up -d
    ```
5.  **Accedi a n8n**:
    Una volta che i container sono in esecuzione, accedi all'interfaccia utente
    di n8n, solitamente all'indirizzo `http://localhost:5678`.
6.  **Importa il Workflow**:
    Importa il file `workflow/pyragogy_master_workflow.json` nella tua istanza
    n8n. Ricorda di attivare il workflow.

Per istruzioni di configurazione più dettagliate, consulta
`docs/setup-quickstart.md`.

## 📚 Documentazione

* [**Note sull'Architettura**](docs/architecture-notes.md): Approfondimento
    sul design del sistema, sui ruoli degli agenti e sui meccanismi di
    interazione.
* [**Guida Rapida all'Installazione**](docs/setup-quickstart.md): Passaggi
    dettagliati per installare ed eseguire il workflow.
* [**Linee Guida per i Contributi**](CONTRIBUTING.md): Come contribuire a
    questo progetto.

## 🤝 Contributo

Accogliamo con favore contributi da sviluppatori, appassionati di AI, content
strategist e chiunque sia interessato alla generazione autonoma di contenuti.
Per maggiori dettagli, consulta `CONTRIBUTING.md`.

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT - consulta il file [LICENSE](LICENSE)
per i dettagli.

## Versioning

Le release sono etichettate usando il formato `vYYYY.MM.DD`. Le voci
dell'Handbook generate dal workflow sono versionate come
`chapter_slug_vTIMESTAMP.md`.

## Changelog

Consulta [CHANGELOG.md](CHANGELOG.md) per la cronologia delle modifiche.

---
