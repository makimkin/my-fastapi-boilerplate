ARG PYTHON_VERSION=3.13.0
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

RUN if [ "$APP_ENV" = "production" ]; then poetry export -o requirements.txt --without-hashes ; else poetry export -o requirements.txt --without-hashes --with=dev ; fi

# ------------------------------------------------------------------------------
# BUILD STAGE
# ------------------------------------------------------------------------------
FROM base AS build

COPY --from=poetry /requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN chown -R app_user:app_group /src

USER app_user

# ------------------------------------------------------------------------------
