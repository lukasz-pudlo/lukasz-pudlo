FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1     PYTHONDONTWRITEBYTECODE=1     UV_SYSTEM_PYTHON=1

WORKDIR /app

RUN apt-get update   && apt-get install --no-install-recommends -y build-essential libpq-dev curl   && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --no-install-project

COPY ./compose/local/django/start /start
COPY ./compose/local/django/celery/worker/start /start-celeryworker
COPY ./compose/local/django/celery/beat/start /start-celerybeat
COPY ./compose/local/django/celery/flower/start /start-flower
RUN chmod +x /start /start-celeryworker /start-celerybeat /start-flower

COPY . /app
