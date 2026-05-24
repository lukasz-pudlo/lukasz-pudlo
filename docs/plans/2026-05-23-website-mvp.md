# Personal Website MVP Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build the first useful version of Lukasz Pudlo's personal website: a distinctive homepage, a portfolio with individual project pages, an about me page, and a contact route.

**Architecture:** Keep this as a small server-rendered Django site. Use the existing `pages` app for static editorial pages, Django templates for layout, HTMX/Hyperscript only where they add a clear interaction, and Tailwind/DaisyUI for styling. Avoid blog/CMS models until there is real content that needs persistence.

**Tech Stack:** Django 6, Python 3.14, pytest, HTMX, Hyperscript, Tailwind CSS, DaisyUI, WhiteNoise, uv.

---

## Design direction

- Keep the MVP minimal.
- Main navbar: `Portfolio`, `Contact`, `About me`.
- Visual style: 1980s computer magazine with a chrome look.
- Portfolio has individual project pages.
- Portfolio pages show tab-like navigation beneath the main navbar.
- Portfolio pages should centre on interactive live embeds of websites Lukasz has built. The page metaphor is a 1980s computer magazine spread with a usable website embedded into the page. Use screenshots/videos as fallbacks when a site cannot be embedded.

## Phase 1: Content shape and navigation

### Task 1: Add route tests for the initial page set

**Objective:** Lock in the first information architecture before changing templates.

**Files:**
- Modify: `lukasz_pudlo/pages/tests/test_views.py`
- Modify later: `lukasz_pudlo/pages/urls.py`
- Modify later: `lukasz_pudlo/pages/views.py`

**Step 1: Write failing tests**

Add tests for these named routes:

- `pages:home`
- `pages:about`
- `pages:projects`
- `pages:contact`

Each test should assert `HTTPStatus.OK` and one distinctive phrase on the page.

**Step 2: Run tests to verify failure**

Run:

```bash
uv run pytest lukasz_pudlo/pages/tests/test_views.py -q
```

Expected: about/projects/contact fail because the routes do not exist yet.

**Step 3: Add minimal routes and views**

Add function-based views in `lukasz_pudlo/pages/views.py` and named paths in `lukasz_pudlo/pages/urls.py`.

**Step 4: Add minimal templates**

Create:

- `lukasz_pudlo/pages/templates/pages/about.html`
- `lukasz_pudlo/pages/templates/pages/projects.html`
- `lukasz_pudlo/pages/templates/pages/contact.html`

**Step 5: Run tests to verify pass**

Run:

```bash
uv run pytest lukasz_pudlo/pages/tests/test_views.py -q
```

Expected: all page tests pass.

---

### Task 2: Add base navigation and footer

**Objective:** Make all initial pages reachable and give the site a coherent shell.

**Files:**
- Modify: `templates/base.html`
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Step 1: Write failing tests**

Assert the homepage includes links to `/about/`, `/projects/`, and `/contact/`.

**Step 2: Run tests to verify failure**

Run:

```bash
uv run pytest lukasz_pudlo/pages/tests/test_views.py -q
```

Expected: fails because the links are not rendered yet.

**Step 3: Implement navigation**

Add a simple header with DaisyUI navbar classes and a footer with a restrained copyright line.

**Step 4: Run tests to verify pass**

Run:

```bash
uv run pytest lukasz_pudlo/pages/tests/test_views.py -q
```

Expected: all tests pass.

---

## Phase 2: Visual direction

### Task 3: Replace placeholder CSS with a proper Tailwind/DaisyUI source pipeline

**Objective:** Move from placeholder static CSS to a maintainable Tailwind/DaisyUI source file.

**Files:**
- Create: `theme/static_src/src/styles.css`
- Create/modify: Tailwind/DaisyUI build configuration as needed by `django-tailwind`
- Modify: `docker-compose.local.yml` if a `tailwind` service is needed
- Modify: `CLAUDE.md` with exact CSS build commands once established

**Step 1: Write a small smoke test**

Add a test that confirms `base.html` references `css/dist/styles.css` and that staticfiles can resolve it.

**Step 2: Run test to verify current behaviour**

Run:

```bash
uv run pytest -q
```

Expected: current static path resolves, but source pipeline is absent.

**Step 3: Implement CSS source pipeline**

Use the acorn_pay pattern where practical, but keep this project simpler unless there is a real need for extra moving parts.

**Step 4: Verify**

Run:

```bash
uv run pytest -q
uv run python manage.py collectstatic --noinput --clear --settings=config.settings.test
```

Expected: tests pass and collectstatic succeeds.

---

### Task 4: Design the homepage as a personal editorial landing page

**Objective:** Give the homepage a polished first draft without pretending the final copy is known.

**Files:**
- Modify: `lukasz_pudlo/pages/templates/pages/home.html`
- Modify: `static/css/dist/styles.css` or the new Tailwind source from Task 3
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Step 1: Write failing content tests**

Assert the homepage contains sections for:

- intro
- current work
- selected projects
- writing/notes
- contact call-to-action

**Step 2: Run tests to verify failure**

Run:

```bash
uv run pytest lukasz_pudlo/pages/tests/test_views.py -q
```

Expected: tests fail until sections exist.

**Step 3: Implement the first draft**

Use a clean editorial layout: strong typography, limited colour palette, and restrained motion. Avoid generic SaaS hero copy. Use placeholders only where content is genuinely unknown.

**Step 4: Run tests and inspect manually**

Run:

```bash
uv run pytest -q
uv run python manage.py runserver
```

Then inspect `http://127.0.0.1:8000/`.

---

## Phase 3: Content and interactive project pages

### Task 5: Draft the About page

**Objective:** Add a structured but editable About page.

**Files:**
- Modify: `lukasz_pudlo/pages/templates/pages/about.html`
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Content sections:**

- short bio
- technical focus
- working principles
- links/contact

Use clearly marked draft copy so Lukasz can replace it.

---

### Task 6: Draft the Projects page

**Objective:** Add a portfolio index without adding a database model prematurely.

**Files:**
- Modify: `lukasz_pudlo/pages/templates/pages/portfolio.html`
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Approach:** Hard-code 2-4 project cards for now. Each card should preview an interactive website exhibit, with a large chrome-framed thumbnail/mini-screen area, project title, short description, and link to an individual project page. Extract to data/model only when maintaining it in templates becomes annoying.

---

### Task 6b: Add interactive individual project pages

**Objective:** Give each project a dedicated magazine-like page designed around an embedded, usable version of the website.

**Files:**
- Modify: `lukasz_pudlo/pages/urls.py`
- Modify: `lukasz_pudlo/pages/views.py`
- Create: `lukasz_pudlo/pages/templates/pages/project_detail.html`
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Approach:** Keep project data as a small in-code list/dictionary for the MVP. Each project page should include:

- tab-like portfolio navigation beneath the main navbar
- a large chrome hero frame for the live embedded website
- an `<iframe>` using a project-specific embed URL where the target site allows framing
- a fallback link and optional screenshot/video when the target site blocks framing with `X-Frame-Options` or `Content-Security-Policy: frame-ancestors`
- clear controls: `Open full site` and `Reload exhibit`
- `sandbox` attributes for the iframe, loosened only as needed per project
- concise project notes below the media
- sensible `loading="lazy"` on images once real assets exist
- native `<video controls preload="metadata">` for videos, not a JavaScript player

---

### Task 7: Draft the Contact page

**Objective:** Add a no-backend contact page that points to preferred channels.

**Files:**
- Modify: `lukasz_pudlo/pages/templates/pages/contact.html`
- Test: `lukasz_pudlo/pages/tests/test_views.py`

**Approach:** Start with email/social links. Do not add a contact form until there is a reason to handle spam, email delivery, and validation.

---

## Verification checklist

Run before considering the MVP complete:

```bash
uv run pytest -q
uv run python manage.py check --settings=config.settings.test
uv run ruff check .
DJANGO_SECRET_KEY=check DJANGO_ALLOWED_HOSTS=example.com,localhost,127.0.0.1 DATABASE_URL=sqlite:////tmp/lukasz-pudlo-check.sqlite3 REDIS_URL=redis://localhost:6379/0 uv run python manage.py check --settings=config.settings.production
```

Manual checks:

- Homepage works at `/`.
- About works at `/about/`.
- Projects works at `/projects/`.
- Contact works at `/contact/`.
- Navigation works without JavaScript.
- Pages remain readable on mobile widths.
- No user-facing American spellings have been introduced.
