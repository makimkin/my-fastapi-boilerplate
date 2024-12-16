# FastAPI Boilerplate (DDD)

![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-A888B5)
![Python](https://img.shields.io/badge/Python-3.12+-8174A0)
[![License](https://img.shields.io/github/license/makimkin/my-fastapi-boilerplate)](https://github.com/makimkin/my-fastapi-boilerplate/blob/main/LICENSE)

A modern FastAPI boilerplate structured around **Domain-Driven Design (DDD)** principles. This project provides a foundation for building scalable, maintainable, and testable web APIs.

## Features

- **FastAPI Framework**: Leverages the performance and ease of use of FastAPI.
- **Domain-Driven Design**: Well-organized codebase for clear separation of concerns.
- **Dependency Injection**: Simplifies component management and testing.
- **Asynchronous I/O**: High performance for modern APIs.
- **Extensible Structure**: Easy to add new domains and features.
- **Testing Ready**: Integrated with `pytest` for unit and integration tests.
- **Environment Management**: `.env` support for configuration.
- **Database Integration**: Pre-configured for relational or NoSQL databases.
- **Docker Support**: Containerized setup for development and production environments.

---

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) (recommended for dependency management)
- Docker (optional, for containerized development)

### Installation

1. Clone the repository:
   ```bash
   cookiecutter git@github.com:makimkin/my-fastapi-boilerplate.git
   cd my-fastapi-boilerplate
   ```

---

## Project Structure

```plaintext
my-fastapi-boilerplate/
├── app/
│   ├── application/          # Application layer (controlcenter of the app)
│   │   ├── api/              # API routes
│   │   └── exceptions.py     # Base application exceptions
│   ├── domain/               # Domain layer (entities, aggregates, value objects, etc.)
│   ├── infrastructure/       # Infrastructure layer (ORM models, database adapters, etc.)
│   ├── services/             # Application services and use cases
│   ├── tests/                # Test cases
│   └── console.py            # Application's console
├── .env                      # Environment variables
├── pyproject.toml            # Poetry configuration
├── justfile                  # Aliases file
├── .pre-commit-config.yaml   # Pre-commit configuration file
├── Dockerfile                # Dockerfile for containerization
├── docker-compose.yml        # Docker Compose for multi-container setup
└── README.md                 # Project documentation
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/makimkin/my-fastapi-boilerplate).

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Domain-Driven Design](https://domainlanguage.com/ddd/)
- [Poetry](https://python-poetry.org/)
