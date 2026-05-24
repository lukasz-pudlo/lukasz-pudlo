# Project: Lukasz Pudlo Personal Website

## Context

Building a personal Django website for Lukasz Pudlo. Working repository/deployment name is `lukasz-pudlo`; Python package name is `lukasz_pudlo`.

## Stack

- Backend: Django 6, Python 3.14
- Frontend: server-rendered templates + HTMX + Hyperscript; no SPA and no JavaScript framework by default
- CSS: Tailwind CSS + DaisyUI
- Database: PostgreSQL 18
- Task queue: Celery + Redis, available when background work is needed
- Email: Anymail/Postmark in deployed environments, Mailpit locally
- Static files: WhiteNoise
- Auth: email-based custom user
- Package management: uv

## House style

- British English in comments, docstrings, and user-facing strings.
- Default to no comments; comment only non-obvious constraints or trade-offs.
- Prefer DaisyUI components, then Tailwind utilities. Avoid bespoke CSS unless it earns its keep.
- Prefer HTMX/Hyperscript patterns over client-side state or a JS framework.

## Website MVP direction

- Keep the first version minimal: homepage, portfolio, contact, and about me.
- Main navbar labels are `Portfolio`, `Contact`, and `About me`.
- Visual direction: 1980s computer magazine with a chrome look — metallic gradients, sharp panels, retro display accents, but still readable and responsive.
- Portfolio projects live on individual pages.
- Inside the portfolio section, show tab-like project navigation beneath the main navbar.
- Optimise project pages for interactive embeds of websites Lukasz has built: each project should feel like a page in a 1980s computer magazine where the featured website can be used inside the page. Use screenshots/videos as fallbacks when a live embed is blocked or inappropriate.

## Testing

- Tests live in per-app `tests/` packages.
- Prefer pytest style with `@pytest.mark.django_db` for database tests.
- Run through Docker by default: `docker compose run --rm django pytest`.
- For view tests, check both expected content and absence of unintended leakage where relevant.

## Deployment pattern

Follow the per-app Hetzner pattern: `/srv/lukasz-pudlo/`, host Nginx/certbot, an isolated Compose stack, embedded app-specific Postgres/Redis, and localhost-bound application ports. Sudo-requiring host steps are performed manually by the user.
