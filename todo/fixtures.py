import pytest
from model_bakery import baker

from .models import Todo


@pytest.fixture
def todo_baker(postgres_container):
    return baker.make(Todo)