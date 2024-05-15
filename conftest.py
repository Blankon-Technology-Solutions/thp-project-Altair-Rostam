import os

import pytest
from django.conf import settings
from rest_framework.test import APIClient
from testcontainers.postgres import PostgresContainer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

pytest_plugins = (
    "todo.fixtures",
)

@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:latest") as container:
        yield container


@pytest.fixture
def api_client():
    return APIClient()
