# Polls API

A REST API for creating and managing polls, built with FastAPI and backed by Upstash Redis.

## Stack

- **FastAPI** — web framework
- **Pydantic v2** — data validation and models
- **Upstash Redis** — serverless Redis for storage
- **uv** — package manager

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

### Setup

```bash
git clone https://github.com/JCYe88/polling-app.git
cd polling-app
uv sync
```

Create a `.env` file in the project root:

```
UPSTASH_REDIS_REST_URL="your-upstash-url"
UPSTASH_REDIS_REST_TOKEN="your-upstash-token"
```

### Run

```bash
uv run uvicorn main:app --reload
```

API docs available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/polls/create` | Create a new poll |
