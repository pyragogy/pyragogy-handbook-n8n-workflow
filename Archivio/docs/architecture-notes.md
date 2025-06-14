# Architecture Notes for Pyragogy n8n Co-Authoring Workflow

## 1. Introduction

This document provides a deep dive into the architectural reasoning behind the
Pyragogy n8n Co-Authoring Workflow. It consolidates design decisions,
highlights non-obvious choices, and outlines the system's operational
principles.

## 2. Context (EN)

The Pyragogy n8n Co-Authoring Workflow is an advanced automation designed to
autonomously compile the Pyragogy Handbook. It integrates GPT-class LLMs
within an n8n orchestration framework, incorporating a human-in-the-loop
(HITL) mechanism for quality assurance.

## 2. Contesto (IT)

Il Workflow di Co-Authoring n8n di Pyragogy è un'automazione avanzata
progettata per compilare autonomamente l'Handbook di Pyragogy. Integra LLM
di classe GPT all'interno di un framework di orchestrazione n8n, incorporando
un meccanismo human-in-the-loop (HITL) per la garanzia della qualità.

---
# (EN) Pyragogy n8n Deep Design (From Previous Iteration)

## Purpose

Consolidate the reasoning behind the proposed multi-agent / human-in-the-loop
automation, highlight non-obvious design decisions, and surface open questions
before implementation.

## 1. Assumptions & Constraints

**Domain**
* **Key Points**: Content Markdown-only; each chapter stored as one file with
    YAML front-matter.
* **Agents**: GPT-class LLMs with function-calling; online search via
    dedicated Researcher agent.
* **Runtime**: n8n self-hosted (Docker) with Postgres + Redis available;
    GitHub repo accessible via PAT.
* **Human Review**: Optional; reviewer responds through secure webhook
    (Slack, TG, e-mail Action).
* **Security**: Secret store holds API keys; network egress restricted;
    GitHub PAT scope repo, workflow.

## 2. High-Level Data Flow

Raw Idea → Meta-Orchestrator → [Summarizer → Synthesizer] ↴
                                              ↘
Online Deep Researcher —> Shared Memory —> Sensemaking Agent —> Peer Review Board
                                                       ↘
                                    Prompt Engineer (refines goals/prompts)
                                                       ↘
                                Explainer & Archivist  →  Human HITL?

* Meta-Orchestrator parses input → creates orchestration plan.json (ordered
    list).
* Dynamic Router iterates plan, invoking each agent function node.
* Shared Memory Layer (Redis hash) stores interim outputs keyed by agent +
    runId. (Note: Current n8n workflow uses `$workflow` variables for state
    management directly, simplifying Redis usage for now).
* After Synthesizer, Researcher may enrich context; other agents can pull
    from Redis. (Note: Researcher agent and direct Redis pulls are currently
    conceptual in the n8n JSON, primarily using `$node` and `$json` for state).
* Peer Review Board = parallel executions of Reviewer, Sensemaking, Prompt
    Engineer. (Note: Implemented sequentially for simplicity in n8n, with a
    consensus step).
* Coordination Node merges feedback → generates Consensus Draft.
* Optionally Pause for human; webhook unblocks flow on approval or returns
    edits.
* Explainer produces learning summary; Archivist commits file + DB row.

## 3. n8n Node Map (minimal)

* HTTP In /chapter – receives JSON `{title,text,requireHitl}`.
* Set → Meta-Orchestrator (OpenAI node w/ function role).
* SplitInBatches to loop through agents (uses plan[index]).
* Switch (dynamic) – resolves agent name → respective sub-workflow.
* Redis SET/GET – read/write shared memory. (Primarily `$workflow` variables
    used for now).
* IF Hitl? – true → Wait (Webhook); false → continue.
* GitHub Create/Update File (octokit wrapper).
* Postgres INSERT for metadata log.
* Slack/TG Notify (optional).

## 4. Coordination & Debate Mechanism

* Use Redis pub/sub channel `run:{id}:board`. (Note: Implemented via direct
    `$node` and `$json` access for consensus check, simplified for n8n).
* Each agent publishes `{agent,output,score}`; a Coordinator function
    aggregates.
* Simple voting: if ≥2 agents flag “major-issue”, loop back to Synthesizer
    with hints.
* Cap at N=2 re-draft loops to avoid infinite cycles.

## 5. Error Handling & Observability

* **API calls**: Retry (3, exp backoff); fallback to shorter prompt; log to Sentry.
* **Router**: On unknown agent → push to Dead-Letter queue + alert.
* **GitHub**: Upsert logic; if merge conflict, append suffix `_v{timestamp}`.
* **Metrics**: Prometheus exporter: run time, tokens, retries, loop count.

## 6. Security Notes

* Store secrets in n8n credential vault; never hard-code.
* Limit Researcher’s HTTP node to allow-listed domains.
* Sanitize markdown to prevent XSS before GitHub commit.

## 7. Scalability Considerations

* Stateless agents → horizontal scale via multiple n8n workers sharing Redis.
* Chunk long chapters (>10k tokens) and process sections in parallel; merge.
* Future: replace Redis with event bus (NATS or Kafka) for high throughput.

## 8. Decisions (Simple Path Chosen)

Following the “best and simplest” principle, we adopt the Alternative A for all
open questions:

| Topic               | Decision                                                         |
| :------------------ | :--------------------------------------------------------------- |
| Consensus Algorithm | Majority-vote: if ≥ 2 agents flag major-issue, loop back to      |
|                     | Synthesizer (max 2 cycles).                                      |
| Cognitive Rhythm    | Minimal YAML tags in front-matter (phase, rhythm).               |
| Tracking            |                                                                  |
| Versioning Strategy | Single main branch; each publish writes/overwrites               |
|                     | chapter_slug_v{timestamp}.md.                                    |
| API-Key / Model     | One shared GPT-4o credential with global rate-limit; all agents  |
| Management          | use same model for now.                                          |

These choices minimise complexity while keeping future upgrades open (e.g.,
switching to weighted scoring or PR-based workflow later).

## 9. Next Steps

* Prototype Dynamic Router sub-workflow.
* Implement Redis shared memory & board pub/sub.
* Draft GitHub + Postgres commit nodes with idempotency.
* Dry-run with dummy chapter; measure tokens & loop latency.
* Review open questions and decide before full production.

## Document version 0.2 — 12 Jun 2025
---
# (IT) Pyragogy n8n Deep Design (Dall'Iterazione Precedente)

## Scopo

Consolidare la logica alla base dell'automazione multi-agente / human-in-the-loop
proposta, evidenziare le decisioni di design non ovvie e far emergere le
questioni aperte prima dell'implementazione.

## 1. Presupposti e Vincoli

**Dominio**
* **Punti Chiave**: Contenuto solo Markdown; ogni capitolo memorizzato come
    un singolo file con YAML front-matter.
* **Agenti**: LLM di classe GPT con funzione-calling; ricerca online tramite
    agente Ricercatore dedicato.
* **Runtime**: n8n self-hosted (Docker) con Postgres + Redis disponibili;
    repo GitHub accessibile tramite PAT.
* **Revisione Umana**: Opzionale; il revisore risponde tramite webhook
    sicuro (Slack, TG, azione via e-mail).
* **Sicurezza**: Il secret store contiene le chiavi API; egress di rete
    ristretto; scope PAT GitHub repo, workflow.

## 2. Flusso Dati di Alto Livello

Idea Grezza → Meta-Orchestrator → [Summarizer → Synthesizer] ↴
                                              ↘
Ricercatore Online Profondo —> Memoria Condivisa —> Agente di Sensemaking —> Commissione di Revisione Paritaria
                                                       ↘
                                    Prompt Engineer (affina obiettivi/prompt)
                                                       ↘
                                Esplicatore & Archivista  →  Human HITL?

* Meta-Orchestrator analizza l'input → crea orchestration plan.json (lista
    ordinata).
* Router Dinamico itera il piano, invocando ciascun nodo funzione dell'agente.
* Strato di Memoria Condivisa (hash Redis) memorizza gli output intermedi
    indicizzati per agente + runId. (Nota: l'attuale workflow n8n utilizza
    direttamente le variabili `$workflow` per la gestione dello stato,
    semplificando l'uso di Redis per ora).
* Dopo il Synthesizer, il Ricercatore può arricchire il contesto; altri
    agenti possono prelevare da Redis. (Nota: l'agente Ricercatore e i
    prelievi diretti da Redis sono attualmente concettuali nel JSON di n8n,
    utilizzando principalmente `$node` e `$json` per lo stato).
* Commissione di Revisione Paritaria = esecuzioni parallele di Revisore,
    Sensemaking, Prompt Engineer. (Nota: Implementato sequenzialmente per
    semplicità in n8n, con un passo di consenso).
* Nodo di Coordinamento unisce il feedback → genera Bozza di Consenso.
* Opzionalmente Pausa per l'umano; il webhook sblocca il flusso
    all'approvazione o restituisce modifiche.
* L'Esplicatore produce un riassunto di apprendimento; l'Archivista
    commette il file + la riga DB.

## 3. Mappa Nodi n8n (minimale)

* HTTP In /chapter – riceve JSON `{title,text,requireHitl}`.
* Set → Meta-Orchestrator (nodo OpenAI con ruolo funzione).
* SplitInBatches per ciclare attraverso gli agenti (usa plan[index]).
* Switch (dinamico) – risolve il nome dell'agente → rispettivo
    sotto-workflow.
* Redis SET/GET – lettura/scrittura memoria condivisa. (Principalmente
    variabili `$workflow` usate per ora).
* IF Hitl? – true → Wait (Webhook); false → continua.
* GitHub Create/Update File (wrapper octokit).
* Postgres INSERT per il log dei metadati.
* Slack/TG Notify (opzionale).

## 4. Meccanismo di Coordinamento e Dibattito

* Usa il canale pub/sub di Redis `run:{id}:board`. (Nota: Implementato
    tramite accesso diretto a `$node` e `$json` per il controllo del
    consenso, semplificato per n8n).
* Ciascun agente pubblica `{agente,output,punteggio}`; una funzione
    Coordinatore aggrega.
* Voto semplice: se ≥2 agenti segnalano “major-issue”, il loop torna al
    Synthesizer con suggerimenti.
* Limite a N=2 cicli di rielaborazione per evitare cicli infiniti.

## 5. Gestione Errori e Osservabilità

* **Chiamate API**: Retry (3, backoff esponenziale); fallback a prompt
    più breve; log su Sentry.
* **Router**: Su agente sconosciuto → push a Dead-Letter queue + alert.
* **GitHub**: Logica di upsert; in caso di conflitto di merge, aggiungi
    suffisso `_v{timestamp}`.
* **Metriche**: Esportatore Prometheus: tempo di esecuzione, token, retry,
    conteggio cicli.

## 6. Note di Sicurezza

* Memorizza i segreti nel vault delle credenziali di n8n; mai hard-code.
* Limita il nodo HTTP del Ricercatore ai domini consentiti.
* Sanitizza il markdown per prevenire XSS prima del commit GitHub.

## 7. Considerazioni sulla Scalabilità

* Agenti stateless → scala orizzontale tramite più worker n8n che
    condividono Redis.
* Suddividi i capitoli lunghi (>10k token) e elabora le sezioni in
    parallelo; unisci.
* Futuro: sostituisci Redis con un event bus (NATS o Kafka) per un
    throughput elevato.

## 8. Decisioni (Percorso Semplice Scelto)

Seguendo il principio del “migliore e più semplice”, adottiamo l'Alternativa A
per tutte le questioni aperte:

| Argomento           | Decisione                                                        |
| :------------------ | :--------------------------------------------------------------- |
| Algoritmo di Consenso | Voto a maggioranza: se ≥ 2 agenti segnalano un problema maggiore, |
|                     | torna al Synthesizer (max 2 cicli).                              |
| Tracciamento Ritmo  | Tag YAML minimali nel front-matter (fase, ritmo).                |
| Cognitivo           |                                                                  |
| Strategia di        | Ramo principale singolo; ogni pubblicazione scrive/sovrascrive   |
| Versioning          | chapter_slug_v{timestamp}.md.                                    |
| Gestione API-Key /  | Un'unica credenziale GPT-4o condivisa con limite di             |
| Modello             | velocità globale; tutti gli agenti usano lo stesso modello per ora.|

Queste scelte minimizzano la complessità pur mantenendo aperte future
opportunità di aggiornamento (es. passare a un punteggio ponderato o a un
workflow basato su PR in seguito).

## 9. Prossimi Passi

* Prototipare il sotto-workflow del Router Dinamico.
* Implementare la memoria condivisa Redis e il pub/sub della board.
* Bozze dei nodi di commit GitHub + Postgres con idempotenza.
* Dry-run con un capitolo fittizio; misurare token e latenza del ciclo.
* Rivedere le questioni aperte e decidere prima della piena produzione.

## Versione del documento 0.2 — 12 Giu 2025
---
