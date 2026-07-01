PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

INSERT OR IGNORE INTO schema_migrations (version, name)
VALUES (1, 'job-search-runtime-v1');

CREATE TABLE IF NOT EXISTS runtime_kv (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE TABLE IF NOT EXISTS run_locks (
    lock_name TEXT PRIMARY KEY,
    owner TEXT NOT NULL,
    acquired_at TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    heartbeat_at TEXT
);

CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    contour TEXT NOT NULL DEFAULT 'job-search',
    trigger_type TEXT NOT NULL,
    source TEXT,
    status TEXT NOT NULL,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    run_log_path TEXT,
    error_summary TEXT,
    metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS processed_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    gmail_message_id TEXT NOT NULL,
    gmail_thread_id TEXT,
    internal_date TEXT,
    header_date TEXT,
    sender TEXT,
    subject TEXT,
    classification TEXT,
    status TEXT NOT NULL DEFAULT 'processed',
    artifact_path TEXT,
    run_id TEXT,
    first_seen_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    last_seen_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    notes TEXT,
    UNIQUE (source, gmail_message_id),
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE INDEX IF NOT EXISTS idx_processed_messages_source_date
ON processed_messages (source, internal_date);

CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    external_id TEXT,
    source_url TEXT,
    company TEXT,
    role TEXT,
    verdict TEXT,
    effort_class TEXT,
    status TEXT NOT NULL DEFAULT 'seen',
    analysis_path TEXT,
    task_path TEXT,
    selected_cv_path TEXT,
    cover_letter_path TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    UNIQUE (source, external_id)
);

CREATE TABLE IF NOT EXISTS vacancy_sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vacancy_id TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_value TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id)
);

CREATE TABLE IF NOT EXISTS telegram_updates (
    update_id TEXT PRIMARY KEY,
    chat_id TEXT,
    message_id TEXT,
    received_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'received',
    run_id TEXT,
    artifact_path TEXT,
    summary TEXT,
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS artifact_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_path TEXT NOT NULL,
    artifact_type TEXT NOT NULL,
    source TEXT,
    source_id TEXT,
    run_id TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    UNIQUE (artifact_path, source, source_id),
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS sync_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    direction TEXT NOT NULL,
    status TEXT NOT NULL,
    git_remote TEXT,
    git_branch TEXT,
    commit_sha TEXT,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    summary TEXT
);
