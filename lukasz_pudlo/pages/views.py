from django.http import Http404
from django.shortcuts import render

PROJECTS = [
    {
        "slug": "south-by-five",
        "title": "South by Five",
        "strapline": "A running club website with a practical publishing surface.",
        "embed_url": "https://southbyfive.run/",
        "summary": (
            "A public website for organising and publishing club activity, presented here as a live "
            "exhibit where framing is allowed."
        ),
        "role": "Django implementation, deployment, content structure",
    },
    {
        "slug": "creek-crosby",
        "title": "Creek Crosby",
        "strapline": "Band website with gigs, media, and merchandise for a rock and roll outfit.",
        "embed_url": "https://creekcrosby.co.uk/",
        "summary": (
            "A website for Creek Crosby, a rock and roll band, covering live dates, "
            "band profiles, music and video, merchandise, and booking."
        ),
        "role": "Django implementation, deployment, visual design",
    },
    {
        "slug": "acorn-pay",
        "title": "Acorn Pay",
        "strapline": "Work-in-progress race-entry payments, receipts, and operational tooling.",
        "status": "Work in progress",
        "embed_url": "https://dev.acornpay.southbyfive.run/",
        "embed_note": (
            "The live exhibit shows the Acorn Pay main page inside this case study. "
            "Account creation and sign-in need third-party cookies that browsers often block inside "
            "iframes, so open the live site directly to create an account or sign in."
        ),
        "summary": (
            "A work-in-progress Django payment system for a small race organisation, built around "
            "Stripe Checkout, email receipts, and replay-safe webhooks."
        ),
        "role": "Architecture, Django implementation, deployment, payment flows",
    },
]


def _project_or_404(slug):
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    msg = "Project not found"
    raise Http404(msg)


def home(request):
    return render(request, "pages/home.html", {"projects": PROJECTS})


def portfolio(request):
    return render(request, "pages/portfolio.html", {"projects": PROJECTS})


def project_detail(request, slug):
    project = _project_or_404(slug)
    idx = next(i for i, p in enumerate(PROJECTS) if p["slug"] == slug)
    next_project = PROJECTS[idx + 1] if idx + 1 < len(PROJECTS) else None
    context = {
        "project": project,
        "projects": PROJECTS,
        "case_num": idx + 1,
        "next_project": next_project,
    }
    return render(request, "pages/project_detail.html", context)


def contact(request):
    return render(request, "pages/contact.html")


def about(request):
    return render(request, "pages/about.html")
