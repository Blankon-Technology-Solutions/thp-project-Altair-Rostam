import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework.test import APIClient

from .models import Todo


@pytest.fixture
def authenticated_api_client():
    # Create a user for authentication
    user = User.objects.create(username="testuser")
    # Create an authenticated client
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    # Clean up after the test
    client.force_authenticate(user=None)
    user.delete()


@pytest.fixture
def todo_baker(postgres_container):
    return baker.make(Todo)
