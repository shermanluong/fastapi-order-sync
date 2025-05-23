# FastAPI Backend Demo

This project is a demonstration of a modern backend API built with **FastAPI**, designed to showcase key backend development skills including async programming, API design, database integration, and testing.

## Features

- Built with **FastAPI** for fast, asynchronous API endpoints
- Async **SQLAlchemy 2.0** integration with **PostgreSQL**
- External API calls using **httpx**
- Database migrations with **Alembic**
- Structured logging using **loguru**
- Robust error handling and validation
- Unit and integration testing with **pytest**
- Auto-generated OpenAPI documentation available at `/docs`

---

## Project Structure
<pre lang="text">
src/├── app/
    │ ├── main.py # Application entrypoint
    │ ├── api/ # API route definitions
    │ ├── models/ # Database models (SQLAlchemy)
    │ ├── schemas/ # Pydantic schemas for request/response validation
    │ ├── services/ # Business logic and third-party API integration
    │ ├── db/ # Database connection and session management
    │ └── core/ # Configuration, logging, utilities
    ├── alembic/ # Database migrations
    ├── tests/ # Test suite
    ├── requirements.txt # Python dependencies
    ├── .env # Environment variables (not included in repo)
    └── README.md
</pre>

---

## Quick Start

### 1. Clone repository

```bash
git clone https://github.com/yourusername/fastapi-backend-demo.git
cd fastapi-backend-demo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```ini
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
DEBUG=True
```
Replace user, password, localhost, 5432, and dbname with your actual database credentials.

### 5. Run database migrations
```bash
alembic upgrade head
```

### 6. Run the application
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs to explore the interactive API documentation.

### 7. Running tests
```bash
pytest tests/
```

## Loggin and Monotoring
- Uses loguru for structured logging
- Easily extensible to integrate with monitoring tools like Grafana, Elasticsearch, or OpenSearch

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 (async)
- Alembic
- httpx
- loguru
- pytest

## Author
Sherman Luong