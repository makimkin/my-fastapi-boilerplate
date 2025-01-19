ARG PYTHON_VERSION=3.13.0

# ------------------------------------------------------------------------------
# BASE STAGE
# ------------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS base

ARG APP_ENV=development
ARG APP_DB=mongo

ENV PYTHONDONTWRITEBYTECODE 1 && \
    PYTHONUNBUFFERED 1

RUN apt update -y

# ------------------------------------------------------------------------------
# USER STAGE
# ------------------------------------------------------------------------------
FROM base AS user

RUN addgroup --system app_group && \
    adduser --system --ingroup app_group app_user

WORKDIR /src

# ------------------------------------------------------------------------------
# POETRY DEPENDENCIES
# ------------------------------------------------------------------------------
FROM base AS dependencies

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry
RUN poetry self add poetry-plugin-export

RUN if [ "$APP_DB" = "postgres" ]; then \
        DB_FLAG="--without-hashes --with=sql"; \
    elif [ "$APP_DB" = "mongo" ]; then \
        DB_FLAG="--without-hashes --with=mongo"; \
    else \
        DB_FLAG="--without-hashes"; \
    fi && \
    if [ "$APP_ENV" = "production" ]; then \
        poetry export -o requirements.txt ${DB_FLAG}; \
    else \
        poetry export -o requirements.txt ${DB_FLAG} --with=dev; \
    fi && \
    echo "APP_DB: ${APP_DB}" && \
    echo "DB_FLAG: ${DB_FLAG}" && \
    echo "APP_ENV: ${APP_ENV}"

# ------------------------------------------------------------------------------
# BUILD STAGE
# ------------------------------------------------------------------------------
FROM user AS build

COPY --from=dependencies /requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN chown -R app_user:app_group /src

USER app_user

# ------------------------------------------------------------------------------
