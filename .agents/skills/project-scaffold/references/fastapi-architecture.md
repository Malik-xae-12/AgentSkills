# FastAPI Modular Domain Architecture

This specification outlines the exact clean, modular architecture for enterprise FastAPI backends. It strictly adheres to the Single Responsibility Principle and enforces a clean layer hierarchy: Router $\rightarrow$ Service $\rightarrow$ Repository $\rightarrow$ Models.

---

## Directory Tree Specification

```text
backend/
│
├── app/                         # Main application source code
│   │
│   ├── main.py                  # Application entry point
│   ├── app_factory.py           # App creation logic (factory pattern)
│   │
│   ├── core/                    # Core system configurations
│   │   ├── config.py            # Environment variables, settings
│   │   ├── security.py          # Password hashing, token helpers
│   │   ├── logging.py           # Logging configuration
│   │   ├── events.py            # Startup & shutdown events
│   │   └── exceptions.py        # Global exception handlers
│   │
│   ├── db/                      # Database layer (shared across modules)
│   │   ├── base.py              # SQLAlchemy Base class
│   │   ├── session.py           # Database session/connection
│   │   └── models_import.py     # Loads all models for Alembic migrations
│   │
│   ├── modules/                 # Feature-based business domains
│   │   │
│   │   ├── auth/                # Authentication feature
│   │   │   ├── router.py        # API endpoints (login, register, etc.)
│   │   │   ├── service.py       # Business logic (auth workflows)
│   │   │   ├── schema.py        # Request/response models
│   │   │   ├── dependency.py    # Auth dependencies (JWT, guards)
│   │   │   └── models/          # Auth-related DB tables (optional)
│   │   │       └── __init__.py  # Model exports
│   │   │
│   │   ├── users/               # User feature module
│   │   │   ├── router.py        # User API endpoints
│   │   │   ├── service.py       # User business logic
│   │   │   ├── schema.py        # User request/response models
│   │   │   ├── repository.py    # User database queries (CRUD)
│   │   │   │
│   │   │   └── models/          # User-related database tables
│   │   │       ├── user.py      # User table model
│   │   │       ├── profile.py   # User profile table
│   │   │       ├── role.py      # Roles/permissions table
│   │   │       └── __init__.py  # Model exports
│   │   │
│   │   ├── items/               # Item/Product feature module
│   │   │   ├── router.py        # Item API endpoints
│   │   │   ├── service.py       # Item business logic
│   │   │   ├── schema.py        # Item request/response models
│   │   │   ├── repository.py    # Item database queries
│   │   │   │
│   │   │   └── models/          # Item-related database tables
│   │   │       ├── item.py      # Item/Product table
│   │   │       ├── category.py  # Category table
│   │   │       └── __init__.py  # Model exports
│   │
│   ├── shared/                  # Common reusable helpers
│   │   ├── responses.py         # Standard API response format
│   │   ├── pagination.py        # Pagination utilities
│   │   └── constants.py         # Global constants
│   │
│   ├── dependencies.py          # Global dependency providers
│   └── middleware.py            # Custom middleware (logging, auth, etc.)
│
├── tests/                       # Automated tests
│   ├── unit/                    # Unit tests (services, utils)
│   └── integration/             # API integration tests
│
├── alembic/                     # Database migrations
├── requirements.txt             # Python dependencies
└── Dockerfile                   # Docker image build file
```

---

## Layer Responsibilities

| Layer | File / Directory | Responsibility | Invariants & Rules |
|---|---|---|---|
| **Router** | `router.py` | Handles HTTP request/response | - Uses `APIRouter`<br>- Defines paths, HTTP methods, status codes, tags<br>- Injects dependencies (DB session, current user)<br>- **Never** executes raw SQL queries or direct DB access<br>- **Never** contains heavy business logic |
| **Service** | `service.py` | Core business logic & workflows | - Coordinates operations across repositories<br>- Performs business validation, password hashing, emails<br>- Handles transaction commit/rollback logic<br>- Returns domain models or schemas, raises domain exceptions |
| **Repository** | `repository.py` | Database operations & queries | - Encapsulates all SQLAlchemy queries and CRUD statements<br>- Accepts `db: Session` or `AsyncSession`<br>- **No** HTTP-related concepts (no `Request`, `Response`, `HTTPException`) |
| **Models** | `models/*.py` | DB table structure | - Inherits from `Base` (`db/base.py`)<br>- Defines table names, columns, indexes, foreign keys, relationships<br>- Re-exported in `models/__init__.py` and registered in `db/models_import.py` |
| **Schemas** | `schema.py` | Data validation & serialization | - Pydantic V2 models (`BaseModel`)<br>- Request schemas (e.g. `UserCreate`, `UserUpdate`, `LoginRequest`)<br>- Response schemas (e.g. `UserResponse`, `TokenResponse`) with `from_attributes = True` |
| **Guards** | `dependency.py` | Module-level dependencies | - Token decoding (`get_current_user`)<br>- Role-based access control (RBAC) guards (`require_role("admin")`) |

---

## Core System Architecture

1. **Application Factory (`app/app_factory.py`)**:
   - Creates the `FastAPI` instance.
   - Registers CORS, logging, exception handlers, and custom middleware.
   - Discovers and includes routers from all modules under `/api/v1/...`.
   - Attaches lifespan event handlers (startup DB ping, connection pool initialization, shutdown cleanup).
2. **Configuration (`app/core/config.py`)**:
   - Uses `pydantic-settings` (`BaseSettings`) to read `.env` with strong type validation (DB URI, JWT secret, environment mode, allowed origins).
3. **Database Layer (`app/db/`)**:
   - `base.py`: Declares SQLAlchemy `DeclarativeBase`.
   - `session.py`: Manages the database engine (`create_engine` or `create_async_engine`) and `sessionmaker`. Provides `get_db` generator dependency.
   - `models_import.py`: Explicitly imports all model modules so Alembic's `target_metadata` detects all tables for autogenerating migrations.
4. **Standard Responses (`app/shared/responses.py`)**:
   - Unifies API response envelopes: `{ "success": true, "data": ..., "message": "...", "meta": { ... } }`.
5. **Testing Architecture (`tests/`)**:
   - `tests/unit/`: Tests individual services, password hashing, and validators in isolation (using mocks).
   - `tests/integration/`: Uses `TestClient` or `AsyncClient` with an in-memory SQLite or test PostgreSQL instance to test complete request/response flows.

