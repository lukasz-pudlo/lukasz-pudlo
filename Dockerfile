FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1     PYTHONDONTWRITEBYTECODE=1     UV_SYSTEM_PYTHON=1     DJANGO_SETTINGS_MODULE=config.settings.production

WORKDIR /app

RUN apt-get update   && apt-get install --no-install-recommends -y build-essential libpq-dev curl   && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY pyproject.toml README.md ./
RUN uv sync --no-dev --no-install-project

COPY . /app

CMD ["sh", "-c", "python manage.py collectstatic --noinput --clear && python manage.py migrate && exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile - --error-logfile -"]
