# {{cookiecutter.app_name.upper()}}

---

## Installation

### For Usage

Set up the environment and install dependencies:

```bash
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
poetry install
```

### For Developers

1. Install [justfile](https://github.com/casey/just)

2. Install environment

```bash
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
poetry install
```

3. Initialize the repository and set up pre-commit hooks:

```bash
git init
rm -rf ./.git/hooks
git clone git@github.com:makimkin/hooks.git ./.git/hooks
pre-commit install
```

# STARTING

#### Docker & MongoDB

Build and run the application in detached mode using Docker:

```bash
export APP_DB=mongo && just up [-d]
```

#### Docker & PostgreSQL

Build and run the application [in detached mode] using Docker, and perform database migrations:

```bash
export APP_DB=postgres && just up [-d]
just app-migration-up
```

# TESTING

Run the tests [with optional output] and [exit on the first failure]:

```bash
just test [-s] [--sw]
```

# SHUTTING DOWN

To shut down the application [and optionally remove its volumes]:

```bash
just down [-v]
```

# USAGE

## Documentation
Once the application is running, you can access:
- **[Swagger UI](http://localhost:8000/docs)**
- **[Redoc](http://localhost:8000/redoc)**


# STRUCTURE

```
my-fastapi-ayomi/
├── .github/
│   └── workflows/
│       └── <GitHub Actions workflows>
├── src/
│   ├── application
│   │   └── <application layer of the project>
│   ├── domain/
│   │   └── <domain layer of the project>
│   ├── interface/
│   │   └── <interface layer>
│   ├── infrastructure/
│   │   └── <infrastructure layer>
│   ├── settings/
│   │   └── <global configuration of the project>
│   ├── tests/
│   │   └── <all test cases>
│   └── lib/
│       └── <utility functions>
├── .env.sample                 # Sample environment configuration file
├── .gitignore                  # Files and folders ignored by Git
├── .pre-commit-config.yaml     # Pre-commit hook configuration
├── Dockerfile                  # Docker image for the application
├── README.md                   # Project documentation
├── docker-compose.app.yaml     # Docker Compose configuration for the application
├── docker-compose.mongo.yaml   # Docker Compose configuration for MongoDB
├── docker-compose.postgres.yaml# Docker Compose configuration for PostgreSQL
├── justfile                    # Task automation script
├── poetry.lock                 # Poetry dependency lock file
└── pyproject.toml              # Python project configuration and dependencies
```
