#!/usr/bin/env python3
"""
Advanced monitoring script for the Pyragogy n8n workflow.
Collects custom metrics and exposes them for Prometheus.
"""

import time
import json
import psycopg2
import redis
import requests
from prometheus_client import start_http_server, Gauge, Counter, Histogram
import os
import logging
from datetime import datetime, timedelta

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus Metrics
workflow_executions_total = Counter('pyragogy_workflow_executions_total', 'Total workflow executions', ['status'])
workflow_duration = Histogram('pyragogy_workflow_duration_seconds', 'Workflow execution duration')
agent_executions_total = Counter('pyragogy_agent_executions_total', 'Total agent executions', ['agent_name', 'status'])
tokens_used_total = Counter('pyragogy_tokens_used_total', 'Total tokens used', ['agent_name'])
cost_total = Counter('pyragogy_cost_usd_total', 'Total cost in USD', ['agent_name'])
redraft_cycles = Histogram('pyragogy_redraft_cycles', 'Number of redraft cycles per workflow')
human_review_pending = Gauge('pyragogy_human_reviews_pending', 'Number of pending human reviews')
human_review_response_time = Histogram('pyragogy_human_review_response_hours', 'Human review response time in hours')
database_entries_total = Gauge('pyragogy_handbook_entries_total', 'Total handbook entries', ['phase'])
error_rate = Gauge('pyragogy_error_rate', 'Error rate in last hour')

class PyragogyMonitor:
    def __init__(self):
        self.db_config = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'port': os.getenv('POSTGRES_PORT', '5432'),
            'database': os.getenv('POSTGRES_DB', 'pyragogy'),
            'user': os.getenv('POSTGRES_USER', 'pyragogy'),
            'password': os.getenv('POSTGRES_PASSWORD', 'pyragogy123')
        }
        
        self.redis_config = {
            'host': os.getenv('REDIS_HOST', 'localhost'),
            'port': int(os.getenv('REDIS_PORT', '6379')),
            'db': 0
        }
        
        self.n8n_url = os.getenv('N8N_URL', 'http://localhost:5678')
        
    def get_db_connection(self):
        """Gets a PostgreSQL database connection"""
        try:
            return psycopg2.connect(**self.db_config)
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            return None
            
    def get_redis_connection(self):
        """Gets a Redis connection"""
        try:
            return redis.Redis(**self.redis_config)
        except Exception as e:
            logger.error(f"Redis connection error: {e}")
            return None
            
    def collect_workflow_metrics(self):
        """Collects workflow metrics"""
        conn = self.get_db_connection()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            
            # Workflow metrics in the last 24 hours
            cursor.execute("""
                SELECT 
                    success,
                    COUNT(*) as count,
                    AVG(total_duration_ms) as avg_duration,
                    AVG(redraft_cycles) as avg_redrafts,
                    SUM(total_tokens_used) as total_tokens,
                    SUM(total_cost_usd) as total_cost
                FROM workflow_metrics 
                WHERE execution_start > NOW() - INTERVAL '24 hours'
                GROUP BY success
            """)
            
            for row in cursor.fetchall():
                success, count, avg_duration, avg_redrafts, total_tokens, total_cost = row
                status = 'success' if success else 'failure'
                
                workflow_executions_total.labels(status=status)._value._value = count or 0
                
                if avg_duration:
                    workflow_duration.observe(avg_duration / 1000)  # Convert to seconds
                    
                if avg_redrafts:
                    redraft_cycles.observe(avg_redrafts)
                    
            # Agent metrics
            cursor.execute("""
                SELECT 
                    agent_name,
                    COUNT(*) as executions,
                    SUM(tokens_used) as total_tokens,
                    SUM(cost_usd) as total_cost
                FROM agent_contributions 
                WHERE created_at > NOW() - INTERVAL '24 hours'
                GROUP BY agent_name
            """)
            
            for row in cursor.fetchall():
                agent_name, executions, total_tokens_agent, total_cost_agent = row
                
                agent_executions_total.labels(agent_name=agent_name, status='success')._value._value = executions or 0
                
                if total_tokens_agent:
                    tokens_used_total.labels(agent_name=agent_name)._value._value = total_tokens_agent
                    
                if total_cost_agent:
                    cost_total.labels(agent_name=agent_name)._value._value = float(total_cost_agent)
                    
            # Pending human reviews
            cursor.execute("SELECT COUNT(*) FROM human_reviews WHERE status = 'pending'")
            pending_reviews = cursor.fetchone()[0]
            human_review_pending.set(pending_reviews)
            
            # Human review response time
            cursor.execute("""
                SELECT AVG(response_time_hours) 
                FROM human_reviews 
                WHERE status = 'approved' OR status = 'rejected'
                AND reviewed_at > NOW() - INTERVAL '7 days'
            """)
            avg_response_time = cursor.fetchone()[0]
            if avg_response_time:
                human_review_response_time.observe(float(avg_response_time))
                
            # Handbook entry count by phase
            cursor.execute("""
                SELECT phase, COUNT(*) 
                FROM handbook_entries 
                WHERE status = 'active'
                GROUP BY phase
            """)
            
            for phase, count in cursor.fetchall():
                database_entries_total.labels(phase=phase).set(count)
                
            # Error rate in the last hour
            cursor.execute("""
                SELECT COUNT(*) 
                FROM error_logs 
                WHERE created_at > NOW() - INTERVAL '1 hour'
            """)
            error_count = cursor.fetchone()[0]
            error_rate.set(error_count)
            
        except Exception as e:
            logger.error(f"Error collecting workflow metrics: {e}")
        finally:
            conn.close()
            
    def collect_n8n_metrics(self):
        """Collects metrics from n8n"""
        try:
            # Check n8n status
            response = requests.get(f"{self.n8n_url}/healthz", timeout=5)
            if response.status_code != 200:
                logger.warning(f"n8n is not responding correctly: {response.status_code}")
                
            # You could add other API calls to n8n here if available
            
        except Exception as e:
            logger.error(f"Error collecting n8n metrics: {e}")
            
    def collect_redis_metrics(self):
        """Collects metrics from Redis"""
        redis_conn = self.get_redis_connection()
        if not redis_conn:
            return
            
        try:
            info = redis_conn.info()
            # You could expose specific Redis metrics here if needed
            logger.debug(f"Redis info: {info.get('used_memory_human', 'N/A')}")
            
        except Exception as e:
            logger.error(f"Error collecting Redis metrics: {e}")
            
    def run_monitoring_cycle(self):
        """Executes a complete metric collection cycle"""
        logger.info("Starting monitoring cycle...")
        
        self.collect_workflow_metrics()
        self.collect_n8n_metrics()
        self.collect_redis_metrics()
        
        logger.info("Monitoring cycle completed")
        
    def start_monitoring(self, port=8000, interval=30):
        """Starts the monitoring server"""
        logger.info(f"Starting Prometheus metrics server on port {port}")
        start_http_server(port)
        
        logger.info(f"Starting monitoring with an interval of {interval} seconds")
        
        while True:
            try:
                self.run_monitoring_cycle()
                time.sleep(interval)
            except KeyboardInterrupt:
                logger.info("Stopping monitoring...")
                break
            except Exception as e:
                logger.error(f"Error in monitoring cycle: {e}")
                time.sleep(interval)

def main():
    """Main function"""
    monitor = PyragogyMonitor()
    
    # Port for Prometheus metrics
    metrics_port = int(os.getenv('METRICS_PORT', '8000'))
    
    # Metric collection interval in seconds
    collection_interval = int(os.getenv('COLLECTION_INTERVAL', '30'))
    
    monitor.start_monitoring(port=metrics_port, interval=collection_interval)

if __name__ == "__main__":
    main()
