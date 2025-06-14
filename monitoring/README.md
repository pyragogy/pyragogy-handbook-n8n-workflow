# Monitoring and Observability

This directory contains the configuration and tools for monitoring the Pyragogy workflow.

## Components

### Prometheus (`prometheus.yml`)

* Configuration for collecting metrics from n8n, PostgreSQL, Redis, and the system
* Configurable scraping interval
* Alerting support

### Grafana

* Dashboard to visualize workflow metrics
* Panels for performance, errors, costs, and resource usage
* Integrated alerting

### Custom Monitor (`monitor.py`)

* Python script to collect workflow-specific metrics
* Exposes custom metrics for Prometheus
* Monitoring includes:

  * Workflow executions (success/failures)
  * AI agent performance
  * Token usage and cost
  * Pending human reviews
  * Errors and latency

### Alert Rules (`alert_rules.yml`)

* Alerting rules for critical conditions
* Notifications for downtime, high latency, and errors

## Starting Monitoring

### With Docker Compose

```bash
# Start all services including monitoring
docker-compose -f scripts/docker-compose-monitoring.yml up -d

# Start only monitoring services
docker-compose -f scripts/docker-compose-monitoring.yml up -d prometheus grafana
```

### Manually

```bash
# Start Prometheus
prometheus --config.file=monitoring/prometheus.yml

# Start custom monitor
cd monitoring
pip install prometheus_client psycopg2-binary redis requests
python monitor.py
```

## Accessing Dashboards

* **Prometheus**: [http://localhost:9090](http://localhost:9090)
* **Grafana**: [http://localhost:3000](http://localhost:3000) (admin/admin)
* **Custom Metrics**: [http://localhost:8000/metrics](http://localhost:8000/metrics)

## Available Metrics

### Workflow

* `pyragogy_workflow_executions_total` – Total workflow executions
* `pyragogy_workflow_duration_seconds` – Execution duration
* `pyragogy_redraft_cycles` – Redraft cycles

### AI Agents

* `pyragogy_agent_executions_total` – Executions per agent
* `pyragogy_tokens_used_total` – Tokens used
* `pyragogy_cost_usd_total` – Costs in USD

### Human Reviews

* `pyragogy_human_reviews_pending` – Pending reviews
* `pyragogy_human_review_response_hours` – Response time

### System

* `pyragogy_handbook_entries_total` – Handbook entries per phase
* `pyragogy_error_rate` – Error rate

## Configured Alerts

* **N8N Down**: n8n is not responding
* **High Failure Rate**: High rate of workflow failures
* **Long Execution**: Excessively long executions
* **Database Down**: PostgreSQL is unavailable
* **High Resource Usage**: High CPU/Memory/Disk usage

## Configuration

### Environment Variables

```bash
# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=pyragogy
POSTGRES_USER=pyragogy
POSTGRES_PASSWORD=pyragogy123

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# n8n
N8N_URL=http://localhost:5678

# Monitoring
METRICS_PORT=8000
COLLECTION_INTERVAL=30
```

### Customizing Alerts

Edit `alert_rules.yml` to add new rules:

```yaml
- alert: CustomAlert
  expr: your_metric > threshold
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "Custom alert triggered"
    description: "Description of the alert"
```

## Grafana Dashboard

### Main Panels

1. **Overview**: General system metrics
2. **Workflow Performance**: Duration, success, failures
3. **Agent Performance**: Performance per agent
4. **Cost Tracking**: Token cost monitoring
5. **Human Reviews**: Status of human reviews
6. **System Resources**: CPU, memory, disk
7. **Error Analysis**: Error analysis and debugging

### Import Dashboard

1. Access Grafana (localhost:3000)
2. Go to "+" → "Import"
3. Upload the JSON files from the `grafana/dashboards/` folder

## Troubleshooting

### Prometheus Not Collecting Metrics

* Verify that the targets are reachable
* Check the `prometheus.yml` configuration
* Inspect Prometheus logs

### Monitor.py Won’t Start

* Install dependencies: `pip install -r requirements.txt`
* Verify database credentials
* Check logs for connection errors

### Grafana Shows No Data

* Confirm Prometheus is set as a data source
* Verify the panel queries are correct
* Ensure Prometheus has data

## Extending Monitoring

To add new metrics:

1. Add the metric to `monitor.py`:

```python
new_metric = Gauge('pyragogy_new_metric', 'Description')
```

2. Implement data collection:

```python
def collect_new_metric(self):
    # Logic to gather data
    value = get_metric_value()
    new_metric.set(value)
```

3. Add the call in the monitoring loop:

```python
def run_monitoring_cycle(self):
    # ... other metrics
    self.collect_new_metric()
```

4. Create Grafana panels to visualize the new metric
