# Contributing to Pyragogy n8n Co-Authoring Workflow

We welcome contributions to the Pyragogy n8n Co-Authoring Workflow!
This document outlines the guidelines for contributing to this project.

---

# Contribuire al Workflow di Co-Authoring n8n di Pyragogy

Accogliamo con favore i contributi al Workflow di Co-Authoring n8n di Pyragogy!
Questo documento delinea le linee guida per contribuire a questo progetto.

## How to Contribute (EN)

1.  **Fork the Repository**: Start by forking the `pyragogy/pyragogy-n8n-workflow`
    repository to your GitHub account.
2.  **Clone Your Fork**:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/pyragogy-n8n-workflow.git](https://github.com/YOUR_USERNAME/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```
3.  **Create a Branch**:
    For new features or bug fixes, create a dedicated branch:
    ```bash
    git checkout -b feature/your-feature-name
    # or hotfix/your-bug-fix
    ```
    For documentation updates, you can often commit directly to `main` if
    you have write access, or create a `docs/your-doc-update` branch.
4.  **Make Your Changes**: Implement your feature, fix the bug, or update the
    documentation.
5.  **Test Your Changes**: Ensure your changes do not break existing
    functionality. If adding new features, include relevant tests.
6.  **Commit Your Changes**: Write clear, concise commit messages.
    ```bash
    git add .
    git commit -m "feat: Add new awesome feature"
    ```
7.  **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```
8.  **Create a Pull Request (PR)**:
    Go to the original `pyragogy/pyragogy-n8n-workflow` repository on GitHub
    and create a new Pull Request from your branch.
    * Ensure your PR targets the `main` branch.
    * Fill out the PR template with as much detail as possible.

## Come Contribuire (IT)

1.  **Fork del Repository**: Inizia creando un fork del repository
    `pyragogy/pyragogy-n8n-workflow` sul tuo account GitHub.
2.  **Clona il Tuo Fork**:
    ```bash
    git clone [https://github.com/TUO_USERNAME/pyragogy-n8n-workflow.git](https://github.com/TUO_USERNAME/pyragogy-n8n-workflow.git)
    cd pyragogy-n8n-workflow
    ```
3.  **Crea un Branch**:
    Per nuove funzionalità o correzioni di bug, crea un branch dedicato:
    ```bash
    git checkout -b feature/nome-della-tua-funzionalita
    # o hotfix/correzione-del-tuo-bug
    ```
    Per gli aggiornamenti della documentazione, puoi spesso commettere
    direttamente su `main` se hai accesso in scrittura, o creare un branch
    `docs/aggiornamento-della-tua-doc`.
4.  **Apporta le Tue Modifiche**: Implementa la tua funzionalità, correggi il
    bug o aggiorna la documentazione.
5.  **Testa le Tue Modifiche**: Assicurati che le tue modifiche non rompano
    le funzionalità esistenti. Se aggiungi nuove funzionalità, includi test
    pertinenti.
6.  **Commetti le Tue Modifiche**: Scrivi messaggi di commit chiari e concisi.
    ```bash
    git add .
    git commit -m "feat: Aggiunta nuova fantastica funzionalità"
    ```
7.  **Esegui il Push sul Tuo Fork**:
    ```bash
    git push origin feature/nome-della-tua-funzionalita
    ```
8.  **Crea una Pull Request (PR)**:
    Vai al repository originale `pyragogy/pyragogy-n8n-workflow` su GitHub
    e crea una nuova Pull Request dal tuo branch.
    * Assicurati che la tua PR abbia come target il branch `main`.
    * Compila il template della PR con quanti più dettagli possibile.

## Branching Strategy (EN)

We follow a simplified branching strategy:

* **`main` branch**: Represents the latest stable and deployable version.
    All features and bug fixes are merged into `main`.
* **Feature Branches (`feature/*`)**: For new features.
* **Hotfix Branches (`hotfix/*`)**: For urgent bug fixes.
* **Documentation Branches (`docs/*`)**: For significant documentation
    overhauls. Minor documentation fixes can be committed directly to `main`.

## Strategia di Branching (IT)

Seguiamo una strategia di branching semplificata:

* **Branch `main`**: Rappresenta l'ultima versione stabile e deployabile.
    Tutte le funzionalità e le correzioni di bug vengono unite in `main`.
* **Branch di Funzionalità (`feature/*`)**: Per le nuove funzionalità.
* **Branch di Hotfix (`hotfix/*`)**: Per le correzioni urgenti di bug.
* **Branch di Documentazione (`docs/*`)**: Per revisioni significative della
    documentazione. Correzioni minori della documentazione possono essere
    commesse direttamente su `main`.

## Code Style and Checks (EN)

* **Markdown Linting**: Ensure your Markdown files adhere to standard
    formatting.
* **n8n Workflow Linting**: (Future) Automatic checks on the n8n JSON
    workflow export.
* **JavaScript Linting**: If any custom JavaScript code is introduced (e.g.,
    in Function nodes), `eslint` might be applied.

## Stile del Codice e Controlli (IT)

* **Linting Markdown**: Assicurati che i tuoi file Markdown aderiscano alla
    formattazione standard.
* **Linting Workflow n8n**: (Futuro) Controlli automatici sull'export JSON
    del workflow n8n.
* **Linting JavaScript**: Se viene introdotto codice JavaScript personalizzato
    (es. nei nodi Function), potrebbe essere applicato `eslint`.
