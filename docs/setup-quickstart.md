# Setup and Quickstart Guide

This guide provides detailed instructions on how to set up and run the
Pyragogy n8n Co-Authoring Workflow locally using Docker.

---

# Guida all'Installazione Rapida

Questa guida fornisce istruzioni dettagliate su come configurare ed eseguire
localmente il Workflow di Co-Authoring n8n di Pyragogy utilizzando Docker.

## Prerequisites (EN)

Before you begin, ensure you have the following installed on your system:

* **Git**: For cloning the repository.
    [Download Git](https://git-scm.com/downloads)
* **Docker & Docker Compose**: For running the n8n, Postgres, and Redis
    containers.
    [Install Docker](https://docs.docker.com/get-docker/)

## Prerequisiti (IT)

Prima di iniziare, assicurati di avere installato sul tuo sistema:

* **Git**: Per clonare il repository.
    [Scarica Git](https://git-scm.com/downloads)
* **Docker & Docker Compose**: Per eseguire i container di n8n, Postgres e Redis.
    [Installa Docker](https://docs.docker.com/get-docker/)

## Setup Steps (EN)

1.  **Clone the Repository**:
    Open your terminal or command prompt and clone the project repository:
    ```bash
    git clone [https://github.com/pyragogy/pyragogy-n8n-workflow.git](https://github.com/pyragogy/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```

2.  **Configure Environment Variables**:
    Create a `.env` file by copying the provided template. This file will
    store your sensitive API keys and configuration settings.
    ```bash
    cp .env.template .env
    ```
    Open the newly created `.env` file in your preferred text editor and
    fill in the placeholder values:

    * `N8N_BASIC_AUTH_USER` and `N8N_BASIC_AUTH_PASSWORD`: For n8n UI access.
    * `N8N_WEBHOOK_URL`: **Crucial** for the Human-in-the-Loop (HITL)
        mechanism. If running locally, it might be `http://localhost:5678`.
        If deployed, use your public n8n URL.
    * `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`: Database
        credentials.
    * `OPENAI_API_KEY`: Your OpenAI API key.
    * `GITHUB_ACCESS_TOKEN`: A GitHub Personal Access Token with `repo` scope.
    * `GITHUB_REPOSITORY_OWNER`, `GITHUB_REPOSITORY_NAME`: Your GitHub
        organization/username and repository name for handbook archiving.
    * `SLACK_WEBHOOK_URL` (optional): For Slack notifications.
    * `EMAIL_SENDER`, `EMAIL_RECEIVER`, `EMAIL_CREDENTIAL_ID`: For sending
        human review emails. You'll need to create an Email Credential in
        the n8n UI (e.g., SMTP) and get its ID.

3.  **Initialize Database (Optional but Recommended)**:
    If you need to set up specific tables for the handbook or agent
    contributions, you can run SQL scripts.
    *(Placeholder for future database initialization scripts)*
    ```bash
    # Example: docker-compose exec postgres psql -U pyragogy_user -d pyragogy_db -f /path/to/init_db.sql
    # You might need to adjust paths or use 'scripts/init_db.sql' after containers are up.
    ```

4.  **Start Services**:
    Navigate to the `scripts/` directory and use Docker Compose to start
    all required services in detached mode:
    ```bash
    docker-compose -f scripts/docker-compose.yml up -d
    ```
    This will start n8n, Postgres, and Redis.

5.  **Access n8n User Interface**:
    Open your web browser and go to `http://localhost:5678` (or your
    `N8N_HOST:N8N_PORT`). Log in using the `N8N_BASIC_AUTH_USER` and
    `N8N_BASIC_AUTH_PASSWORD` from your `.env` file.

6.  **Import the n8n Workflow**:
    Inside the n8n UI:
    * Click on "Workflows" in the left sidebar.
    * Click "New" or the "Import" button.
    * Select "Import from JSON".
    * Copy the content of `workflow/pyragogy_master_workflow.json` from this
        repository and paste it into the JSON import dialog.
    * Click "Import".
    * **Activate the workflow** by toggling the switch in the top right
        corner of the workflow editor.

7.  **Test the Workflow**:
    You can test the workflow by sending a `POST` request to the webhook URL
    defined in your workflow (e.g., `http://localhost:5678/webhook/pyragogy/process`).
    Example `curl` command:
    ```bash
    curl -X POST \
      http://localhost:5678/webhook/pyragogy/process \
      -H 'Content-Type: application/json' \
      -d '{
        "title": "Introduction to AI Agents",
        "text": "Artificial intelligence agents are autonomous entities...",
        "tags": ["AI", "Agents", "Handbook"],
        "requireHitl": true
      }'
    ```
    Monitor the execution in the n8n UI. If `requireHitl` is true, check the
    `EMAIL_RECEIVER` inbox for the review request.

## Passaggi di Configurazione (IT)

1.  **Clona il Repository**:
    Apri il tuo terminale o prompt dei comandi e clona il repository del progetto:
    ```bash
    git clone [https://github.com/pyragogy/pyragogy-n8n-workflow.git](https://github.com/pyragogy/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```

2.  **Configura le Variabili d'Ambiente**:
    Crea un file `.env` copiando il template fornito. Questo file memorizzerà
    le tue chiavi API sensibili e le impostazioni di configurazione.
    ```bash
    cp .env.template .env
    ```
    Apri il file `.env` appena creato nel tuo editor di testo preferito e
    inserisci i valori placeholder:

    * `N8N_BASIC_AUTH_USER` e `N8N_BASIC_AUTH_PASSWORD`: Per l'accesso
        all'interfaccia utente di n8n.
    * `N8N_WEBHOOK_URL`: **Fondamentale** per il meccanismo Human-in-the-Loop
        (HITL). Se eseguito localmente, potrebbe essere `http://localhost:5678`.
        Se distribuito, usa il tuo URL pubblico di n8n.
    * `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`: Credenziali del
        database.
    * `OPENAI_API_KEY`: La tua chiave API OpenAI.
    * `GITHUB_ACCESS_TOKEN`: Un Personal Access Token di GitHub con scope `repo`.
    * `GITHUB_REPOSITORY_OWNER`, `GITHUB_REPOSITORY_NAME`: La tua
        organizzazione/nome utente GitHub e il nome del repository per
        l'archiviazione dell'Handbook.
    * `SLACK_WEBHOOK_URL` (opzionale): Per le notifiche Slack.
    * `EMAIL_SENDER`, `EMAIL_RECEIVER`, `EMAIL_CREDENTIAL_ID`: Per l'invio
        di email di revisione umana. Dovrai creare una Credenziale Email
        nell'interfaccia utente di n8n (es. SMTP) e ottenere il suo ID.

3.  **Inizializza il Database (Opzionale ma Consigliato)**:
    Se devi impostare tabelle specifiche per l'Handbook o i contributi degli
    agenti, puoi eseguire script SQL.
    *(Placeholder per futuri script di inizializzazione del database)*
    ```bash
    # Esempio: docker-compose exec postgres psql -U pyragogy_user -d pyragogy_db -f /path/to/init_db.sql
    # Potrebbe essere necessario regolare i percorsi o usare 'scripts/init_db.sql'
    # dopo l'avvio dei container.
    ```

4.  **Avvia i Servizi**:
    Naviga nella directory `scripts/` e usa Docker Compose per avviare tutti
    i servizi richiesti in modalità detached:
    ```bash
    docker-compose -f scripts/docker-compose.yml up -d
    ```
    Questo avvierà n8n, Postgres e Redis.

5.  **Accedi all'Interfaccia Utente di n8n**:
    Apri il tuo browser web e vai su `http://localhost:5678` (o il tuo
    `N8N_HOST:N8N_PORT`). Accedi utilizzando `N8N_BASIC_AUTH_USER` e
    `N8N_BASIC_AUTH_PASSWORD` dal tuo file `.env`.

6.  **Importa il Workflow di n8n**:
    All'interno dell'interfaccia utente di n8n:
    * Clicca su "Workflows" nella barra laterale sinistra.
    * Clicca sul pulsante "New" o "Import".
    * Seleziona "Import from JSON".
    * Copia il contenuto di `workflow/pyragogy_master_workflow.json` da
        questo repository e incollalo nella finestra di dialogo di importazione JSON.
    * Clicca su "Import".
    * **Attiva il workflow** tramite l'interruttore nell'angolo in alto a destra
        dell'editor del workflow.

7.  **Testa il Workflow**:
    Puoi testare il workflow inviando una richiesta `POST` all'URL del
    webhook definito nel tuo workflow (es. `http://localhost:5678/webhook/pyragogy/process`).
    Esempio di comando `curl`:
    ```bash
    curl -X POST \
      http://localhost:5678/webhook/pyragogy/process \
      -H 'Content-Type: application/json' \
      -d '{
        "title": "Introduzione agli Agenti AI",
        "text": "Gli agenti di intelligenza artificiale sono entità autonome...",
        "tags": ["AI", "Agenti", "Handbook"],
        "requireHitl": true
      }'
    ```
    Monitora l'esecuzione nell'interfaccia utente di n8n. Se `requireHitl`
    è true, controlla la casella di posta di `EMAIL_RECEIVER` per la
    richiesta di revisione.
