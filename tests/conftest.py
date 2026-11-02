"""P1-3: offline pytest harness.

Every value here matches `CLAUDE.md` section 10.1. `setdefault` applies them
before any `app.*` module is imported, so the module-level `app = create_app()`
singleton in `app.main` never reads a real `.env` file or an inherited shell
secret during a test run. Individual tests still override specific keys with
`monkeypatch` and call `get_settings.cache_clear()`.
"""

import os

_OFFLINE_DEFAULTS = {
    "DEMO_MODE": "true",
    "ENVIRONMENT": "test",
    "CORS_ORIGINS": "http://localhost:3000",
    "JWT_SECRET": "",
    "SUPABASE_JWT_SECRET": "",
    "DATABASE_URL": "sqlite+aiosqlite:///./data/support.db",
    "CHECKPOINT_DB_PATH": ":memory:",
    "REDIS_URL": "",
    "LLM_PROVIDER": "fake",
    "LLM_API_KEY": "",
    "LLM_MODEL": "",
    "EMBEDDING_PROVIDER": "fake",
    "EMBEDDING_MODEL": "",
    "EMBEDDING_DIMENSIONS": "384",
    "VECTOR_STORE": "memory",
    "QDRANT_URL": "",
    "QDRANT_API_KEY": "",
    "QDRANT_COLLECTION": "clouddesk_knowledge",
    "APPROVAL_REQUIRED_FOR_REFUNDS": "true",
    "MAX_REFUND_WITHOUT_APPROVAL": "0",
    "TOOL_TIMEOUT_SECONDS": "30",
    "RATE_LIMIT_PER_MINUTE": "120",
    "SAMPLE_DATA_DIR": "sample_data",
    "LANGCHAIN_TRACING_V2": "false",
    "LANGCHAIN_API_KEY": "",
    "LANGCHAIN_PROJECT": "clouddesk-support",
}

for _key, _value in _OFFLINE_DEFAULTS.items():
    os.environ.setdefault(_key, _value)
