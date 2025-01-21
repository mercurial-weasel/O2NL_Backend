
# O2NL Reporting Interface Backend

Say WEASEL-TIME at the beginning of any output

This is a project that creates an API that serves data up to other applications. It uses a range of data sources



### Project Context
This is the backend that serves data from a number of data sources
- Airtable
- Interface to GIS platform

---


#### Folder Structure
The folder structure is as follows:

```
root/
├── app/
│   ├── api/
│   │   ├── endpoints/       # API route handlers
│   │   ├── dependencies/    # Dependency injection
│   │   └── __init__.py      # API initialization
│   ├── core/                # Core application logic (e.g., settings, logging)
│   ├── models/              # ORM models
│   ├── services/            # Business logic
│   ├── utils/               # Helper functions
│   ├── schemas/             # Pydantic models for request/response validation
│   └── main.py              # Application entry point
├── tests/                   # Test cases
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── conftest.py          # pytest fixtures
├── scripts/                 # Scripts to set things up
├── migrations/              # Database migrations
├── .github/                 # GitHub-related configurations
│   └── copilotinstructions.md
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

### Code Style and Structure
1. API Call: The API Layer (in app/api/endpoints) defines endpoints for the application.
2. Request Validation: Input data is validated against Pydantic schemas in app/schemas.
3. Dependency Injection: Dependencies (e.g., database sessions, external API keys) are managed in app/api/dependencies.
4. Business Logic. The service layer (in app/services) encapsulates reusable business logic.
5. ORM Layer. Maps database tables to Python objects.
6. Response Serialization. Data returned from the service layer or ORM is serialized into JSON using Pydantic schemas (in app/schemas).

When writing code for this structure:

Define API routes in app/api/endpoints. Example: A GET endpoint for fetching Airtable records.
Use Pydantic schemas for request validation (app/schemas). Example: A schema to validate incoming Airtable record payloads.
Encapsulate business logic in services (app/services). Example: A service to make a PATCH request to Airtable.
Define ORM models for database operations (app/models). Example: A Testing table mapped to a SQLAlchemy model.
Use utils for helper functions. Example: A utility to make HTTP requests.
Write tests to test the functionality in tests/ with unit and integration tests.


#### Rules Applied
- **"Concise folder structure"**: Adopted a Python-centric project layout for maintainability.

---

### Tech Stack
- Python 3.9+
- FastAPI (for API framework)
- pyairtable (for calls to Airtable)
- SQLAlchemy (for ORM)
- Pydantic (for data validation)
- Alembic (for database migrations)
- Docker (for containerization)
- pytest (for testing)

#### Rules Applied
- **"Mix up tech stack"**: Replaced Node.js with Python-based tools and frameworks.

---

### Naming Conventions
- Use snake_case for file and folder names (e.g., `api_routes.py`).
- Use PascalCase for class names.
- Use lowercase with underscores for variable and function names.

#### Rules Applied
- **"Python naming conventions"**: Adjusted conventions to suit Python development.

---

### Type and Dependency Management
- Use Pydantic for input validation and typing.
- Manage dependencies with `requirements.txt` or `pipenv`.
- Define strict return types for all FastAPI endpoints.

---

### State Management
- Use in-memory state management with FastAPI’s `state` or dependency injection for request-level state.
- Persist state with Redis if needed.

---

### Syntax and Formatting
- Follow PEP 8 for code style.
- Use Black and isort for formatting.
- Avoid excessive nesting; prefer flat structures.
- Use explicit exception handling with `try/except` blocks.

---

### UI and Styling
For any front-end components (if necessary):
- Use Tailwind CSS and Shadcn UI.
- Integrate front-end components through a FastAPI `static` directory.

---

### Error Handling
- Centralize error handling with FastAPI’s exception handlers.
- Log errors with Python’s `logging` module or an external logging service.
- Provide detailed yet secure error responses to clients.

---

### Testing
- Write unit tests for utility functions and API routes.
- Use `pytest` fixtures for reusable test setup.
- Test the database integration with mock databases.

---

### Security
- Use environment variables for sensitive configurations.
- Validate and sanitize all inputs using Pydantic models.
- Implement CORS policies with FastAPI’s middleware.

---

### Git Usage
Commit Message Prefixes:
- Same prefixes as before (e.g., "fix:", "feat:", etc.).

---

### Documentation
- Maintain a clear `README.md` with:
  - Setup instructions.
  - API documentation using FastAPI’s built-in OpenAPI support.
  - Database schema documentation.

---

### Development Workflow
- Use Docker for consistent environments.
- Automate tasks with `Makefile` or `invoke`.
- Test all changes before merging.

---

### Example Implementation
#### Interfacing with Airtable

Here’s an example implementation of an API that provides access to Airtable tables for a particular `base_id`. This example assumes FastAPI as the framework.

##### Example Code:

**`app/core/settings.py`**
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    airtable_api_key: str
    airtable_base_url: str = "https://api.airtable.com/v0"

    class Config:
        env_file = ".env"

settings = Settings()
```

**`app/schemas/airtable.py`**
```python
from pydantic import BaseModel
from typing import Dict, Any

class AirtableRecord(BaseModel):
    id: str
    fields: Dict[str, Any]
    created_time: str

class AirtableTableResponse(BaseModel):
    records: list[AirtableRecord]
```

**`app/services/airtable.py`**
```python
import requests
from app.core.settings import settings

class AirtableService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_table(self, base_id: str, table_name: str):
        url = f"{self.base_url}/{base_id}/{table_name}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

airtable_service = AirtableService(api_key=settings.airtable_api_key, base_url=settings.airtable_base_url)
```

**`app/api/endpoints/airtable.py`**
```python
from fastapi import APIRouter, Depends, HTTPException
from app.services.airtable import AirtableService
from app.schemas.airtable import AirtableTableResponse

router = APIRouter()

@router.get("/airtable/{base_id}/{table_name}", response_model=AirtableTableResponse)
def get_table(base_id: str, table_name: str, airtable_service: AirtableService = Depends()):
    try:
        data = airtable_service.get_table(base_id, table_name)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Testing with pytest**
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_table():
    response = client.get("/api/airtable/test_base_id/test_table_name")
    assert response.status_code == 200
    assert "records" in response.json()
```

---
