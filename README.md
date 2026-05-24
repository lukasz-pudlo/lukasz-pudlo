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

The local portfolio is served at `http://localhost:8010/`. Target Django projects
that are embedded in portfolio case-study pages should allow iframe ancestors
`http://localhost:8010` and `http://127.0.0.1:8010` during local development.

Run tests:

```bash
docker compose run --rm django pytest
# native alternative, when DATABASE_URL points at Postgres:
uv run pytest
```
