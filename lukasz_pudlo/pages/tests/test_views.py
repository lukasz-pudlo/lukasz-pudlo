from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    ("url_name", "expected"),
    [
        ("pages:home", b"Lukasz Pudlo"),
        ("pages:portfolio", b"Portfolio"),
        ("pages:contact", b"Contact"),
        ("pages:about", b"About"),
    ],
)
def test_core_pages_render(client, url_name, expected):
    response = client.get(reverse(url_name))

    assert response.status_code == HTTPStatus.OK
    assert expected in response.content


def test_main_navigation_uses_minimal_labels(client):
    response = client.get(reverse("pages:home"))

    assert b"Portfolio" in response.content
    assert b"Contact" in response.content
    assert b"About" in response.content
    assert b'href="/portfolio/"' in response.content
    assert b'href="/contact/"' in response.content
    assert b'href="/about/"' in response.content


def test_portfolio_lists_projects_as_linked_cards(client):
    response = client.get(reverse("pages:portfolio"))

    assert response.status_code == HTTPStatus.OK
    assert b"Acorn Pay" in response.content
    assert b"South by Five" in response.content
    assert b"Creek Crosby" in response.content
    assert b'href="/portfolio/acorn-pay/"' in response.content
    assert b'href="/portfolio/south-by-five/"' in response.content
    assert b'href="/portfolio/creek-crosby/"' in response.content
    assert b"story-card" in response.content


def test_project_detail_page_has_live_embed_and_case_tabs(client):
    response = client.get(reverse("pages:project_detail", kwargs={"slug": "acorn-pay"}))

    assert response.status_code == HTTPStatus.OK
    assert b"Acorn Pay" in response.content
    assert b"case-tabs" in response.content
    assert b"<iframe" in response.content
    assert b"sandbox=" in response.content
    assert b"OPEN LIVE SITE" in response.content
    assert b"Reload" in response.content


def test_unknown_project_returns_404(client):
    response = client.get(reverse("pages:project_detail", kwargs={"slug": "unknown"}))

    assert response.status_code == HTTPStatus.NOT_FOUND
