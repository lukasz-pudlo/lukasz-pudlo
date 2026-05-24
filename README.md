# lukasz-pudlo

Personal website for Lukasz Pudlo.

Working-name conventions:

- Repository/deployment name: `lukasz-pudlo`
- Python/Django package name: `lukasz_pudlo`

## Local development

```bash
uv sync
# or use the Docker workflow once Docker images are built:
docker compose up
```

Run tests:

```bash
docker compose run --rm django pytest
# native alternative, when DATABASE_URL points at Postgres:
uv run pytest
```
