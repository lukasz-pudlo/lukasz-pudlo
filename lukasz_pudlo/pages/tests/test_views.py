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


def test_contact_email_button_includes_copy_control(client):
    response = client.get(reverse("pages:contact"))

    assert response.status_code == HTTPStatus.OK
    assert b'href="mailto:lukasz.hubert.pudlo@gmail.com"' in response.content
    assert b'aria-label="Copy email address"' in response.content
    assert b'data-email="lukasz.hubert.pudlo@gmail.com"' in response.content
    assert b"navigator.clipboard.writeText" in response.content
    assert b'id="copy-email-status"' in response.content
    assert b'aria-live="polite"' in response.content
    assert b"Copied to clipboard" in response.content


def test_portfolio_lists_projects_as_linked_cards(client):
    response = client.get(reverse("pages:portfolio"))

    assert response.status_code == HTTPStatus.OK
    content = response.content
    assert content.index(b"South by Five") < content.index(b"Creek Crosby") < content.index(b"Acorn Pay")
    assert b'href="/portfolio/south-by-five/"' in content
    assert b'href="/portfolio/creek-crosby/"' in content
    assert b'href="/portfolio/acorn-pay/"' in content
    assert b"story-card" in content


def test_portfolio_story_cards_show_project_main_pages(client):
    response = client.get(reverse("pages:portfolio"))

    assert response.status_code == HTTPStatus.OK
    assert response.content.count(b"<iframe") == 3
    assert b'src="https://southbyfive.run/"' in response.content
    assert b'src="https://creekcrosby.co.uk/"' in response.content
    assert b'src="https://dev.acornpay.southbyfive.run/"' in response.content
    assert b'title="South by Five main page"' in response.content


def test_project_detail_page_has_live_embed_and_case_tabs(client):
    response = client.get(reverse("pages:project_detail", kwargs={"slug": "acorn-pay"}))

    assert response.status_code == HTTPStatus.OK
    assert b"Acorn Pay" in response.content
    assert b"case-tabs" in response.content
    assert b"<iframe" in response.content
    assert b"sandbox=" in response.content
    assert b"OPEN LIVE SITE" in response.content
    assert b"Reload" in response.content


def test_acorn_pay_case_marks_work_in_progress_and_explains_auth_limit(client):
    response = client.get(reverse("pages:project_detail", kwargs={"slug": "acorn-pay"}))

    assert response.status_code == HTTPStatus.OK
    assert b"Work in progress" in response.content
    assert b"shows the Acorn Pay main page" in response.content
    assert b"open the live site directly to create an account or sign in" in response.content


def test_unknown_project_returns_404(client):
    response = client.get(reverse("pages:project_detail", kwargs={"slug": "unknown"}))

    assert response.status_code == HTTPStatus.NOT_FOUND
