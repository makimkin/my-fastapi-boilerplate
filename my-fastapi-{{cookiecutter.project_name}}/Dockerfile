ARG PYTHON_VERSION=3.12.8
ARG APP_ENV=development

# ------------------------------------------------------------------------------
# BASE STAGE
# ------------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE 1 && \
    PYTHONUNBUFFERED 1

RUN apt update -y

RUN addgroup --system app_group && \
    adduser --system --ingroup app_group app_user

WORKDIR /src

# ------------------------------------------------------------------------------
# POETRY STAGE
# ------------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS poetry

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry
RUN poetry self add poetry-plugin-export

RUN if [ "$APP_ENV" = "development" ]; then poetry export -o requirements.txt --without-hashes --with=dev; else poetry export -o requirements.txt --without-hashes; fi

# ------------------------------------------------------------------------------
# BUILD STAGE
# ------------------------------------------------------------------------------
FROM base AS build

COPY --from=poetry /requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R app_user:app_group /src

USER app_user

# ------------------------------------------------------------------------------
