import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework.test import APIClient

from .models import Todo


@pytest.fixture
def authenticated_user():
    user = User.objects.create_user(username="testuser", password="testpassword")
    yield user
    user.delete()

@pytest.fixture
def authenticated_api_client(authenticated_user):
    client = APIClient()
    client.force_authenticate(user=authenticated_user)
    yield client
    client.force_authenticate(user=None)

@pytest.fixture
def todo_baker(authenticated_user):
    return baker.make(Todo, user=authenticated_user, _quantity=5)
