-- Inizializzazione del database per Pyragogy Handbook
-- Questo script crea le tabelle necessarie per il workflow

-- Tabella per le voci dell'handbook
CREATE TABLE IF NOT EXISTS handbook_entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    version INTEGER DEFAULT 1,
    created_by VARCHAR(100) DEFAULT 'AI Village',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tags TEXT[] DEFAULT '{}',
    phase VARCHAR(50) DEFAULT 'draft',
    rhythm VARCHAR(50) DEFAULT 'on-demand',
    status VARCHAR(50) DEFAULT 'active',
    github_path VARCHAR(500),
    review_status VARCHAR(50) DEFAULT 'pending'
);

-- Tabella per i contributi degli agenti
CREATE TABLE IF NOT EXISTS agent_contributions (
    id SERIAL PRIMARY KEY,
    entry_id INTEGER REFERENCES handbook_entries(id) ON DELETE CASCADE,
    agent_name VARCHAR(100) NOT NULL,
    contribution_type VARCHAR(100) NOT NULL,
    details JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_time_ms INTEGER,
    tokens_used INTEGER,
    cost_usd DECIMAL(10,4)
);

-- Tabella per le metriche del workflow
CREATE TABLE IF NOT EXISTS workflow_metrics (
    id SERIAL PRIMARY KEY,
    workflow_run_id UUID NOT NULL,
    execution_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_end TIMESTAMP,
    total_duration_ms INTEGER,
    agents_executed TEXT[],
    redraft_cycles INTEGER DEFAULT 0,
    human_review_required BOOLEAN DEFAULT false,
    human_review_status VARCHAR(50),
    total_tokens_used INTEGER DEFAULT 0,
    total_cost_usd DECIMAL(10,4) DEFAULT 0,
    error_count INTEGER DEFAULT 0,
    success BOOLEAN DEFAULT true,
    metadata JSONB
);

-- Tabella per i log degli errori
CREATE TABLE IF NOT EXISTS error_logs (
    id SERIAL PRIMARY KEY,
    workflow_run_id UUID,
    agent_name VARCHAR(100),
    error_type VARCHAR(100),
    error_message TEXT,
    stack_trace TEXT,
    context JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    severity VARCHAR(20) DEFAULT 'error'
);

-- Tabella per le revisioni umane
CREATE TABLE IF NOT EXISTS human_reviews (
    id SERIAL PRIMARY KEY,
    review_id UUID UNIQUE NOT NULL,
    entry_id INTEGER REFERENCES handbook_entries(id),
    reviewer_email VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending',
    comments TEXT,
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed_at TIMESTAMP,
    response_time_hours DECIMAL(10,2)
);

-- Indici per migliorare le performance
CREATE INDEX IF NOT EXISTS idx_handbook_entries_created_at ON handbook_entries(created_at);
CREATE INDEX IF NOT EXISTS idx_handbook_entries_tags ON handbook_entries USING GIN(tags);
CREATE INDEX IF NOT EXISTS idx_handbook_entries_phase ON handbook_entries(phase);
CREATE INDEX IF NOT EXISTS idx_agent_contributions_entry_id ON agent_contributions(entry_id);
CREATE INDEX IF NOT EXISTS idx_agent_contributions_agent_name ON agent_contributions(agent_name);
CREATE INDEX IF NOT EXISTS idx_workflow_metrics_run_id ON workflow_metrics(workflow_run_id);
CREATE INDEX IF NOT EXISTS idx_workflow_metrics_execution_start ON workflow_metrics(execution_start);
CREATE INDEX IF NOT EXISTS idx_error_logs_workflow_run_id ON error_logs(workflow_run_id);
CREATE INDEX IF NOT EXISTS idx_error_logs_created_at ON error_logs(created_at);
CREATE INDEX IF NOT EXISTS idx_human_reviews_review_id ON human_reviews(review_id);
CREATE INDEX IF NOT EXISTS idx_human_reviews_status ON human_reviews(status);

-- Trigger per aggiornare updated_at automaticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_handbook_entries_updated_at 
    BEFORE UPDATE ON handbook_entries 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Vista per statistiche rapide
CREATE OR REPLACE VIEW workflow_stats AS
SELECT 
    DATE(execution_start) as date,
    COUNT(*) as total_runs,
    COUNT(*) FILTER (WHERE success = true) as successful_runs,
    COUNT(*) FILTER (WHERE success = false) as failed_runs,
    AVG(total_duration_ms) as avg_duration_ms,
    AVG(redraft_cycles) as avg_redraft_cycles,
    SUM(total_tokens_used) as total_tokens,
    SUM(total_cost_usd) as total_cost
FROM workflow_metrics 
GROUP BY DATE(execution_start)
ORDER BY date DESC;

-- Vista per performance degli agenti
CREATE OR REPLACE VIEW agent_performance AS
SELECT 
    agent_name,
    COUNT(*) as total_contributions,
    AVG(execution_time_ms) as avg_execution_time,
    AVG(tokens_used) as avg_tokens_used,
    SUM(cost_usd) as total_cost,
    COUNT(*) FILTER (WHERE contribution_type LIKE '%Approved%') as approved_contributions
FROM agent_contributions 
GROUP BY agent_name
ORDER BY total_contributions DESC;

-- Inserimento di dati di esempio (opzionale)
INSERT INTO handbook_entries (title, content, tags, phase, rhythm) VALUES 
('Esempio di Capitolo', 'Questo è un esempio di contenuto generato dal workflow AI.', 
 ARRAY['esempio', 'test'], 'draft', 'on-demand')
ON CONFLICT DO NOTHING;

-- Commenti per la documentazione
COMMENT ON TABLE handbook_entries IS 'Memorizza le voci principali dell''handbook generate dal workflow';
COMMENT ON TABLE agent_contributions IS 'Traccia i contributi di ogni agente AI al processo';
COMMENT ON TABLE workflow_metrics IS 'Metriche di performance e monitoraggio del workflow';
COMMENT ON TABLE error_logs IS 'Log degli errori per debugging e monitoraggio';
COMMENT ON TABLE human_reviews IS 'Traccia le revisioni umane richieste e completate';

-- Funzione per pulire i log vecchi (da eseguire periodicamente)
CREATE OR REPLACE FUNCTION cleanup_old_logs(days_to_keep INTEGER DEFAULT 30)
RETURNS INTEGER AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM error_logs 
    WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 day' * days_to_keep;
    
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    
    RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

