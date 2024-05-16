import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_authenticated_todo_view(authenticated_user, client):
    client.force_login(authenticated_user)
    response = client.get("/dashboard/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthenticated_todo_view(client):
    url = reverse("todo")
    response = client.get(url)

    assert response.status_code == 302
    assert response.url.startswith("/accounts/login/")


@pytest.mark.django_db
def test_authenticated_profile_view(authenticated_user, client):
    client.force_login(authenticated_user)
    response = client.get("/accounts/profile/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthenticated_profile_view(client):
    url = reverse("profile")
    response = client.get(url)

    assert response.status_code == 302
    assert response.url.startswith("/accounts/login/")
