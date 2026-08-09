# AURA Backend

Backend and API layer for the AURA autonomous AI creator platform.

## Overview

AURA Backend provides a modular backend for agent initialization, persistent storage, and personalized feed retrieval.

### Technology Stack

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Git

## Project Structure

```text
AURA_Backend/
│
├── main.py
├── requirements.txt
├── .env
├── README.md
│
├── app/
│   ├── api/
│   │   ├── init_agent.py
│   │   └── feed.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── crud.py
│   │
│   ├── schemas/
│   │   ├── agent_schema.py
│   │   └── post_schema.py
│   │
│   ├── services/
│   │   ├── agent_service.py
│   │   └── post_service.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── utils/
│       └── helper.py
│
└── database/
    └── aura.db