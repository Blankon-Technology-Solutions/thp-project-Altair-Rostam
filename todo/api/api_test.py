import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from ..models import Todo


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def todo_baker():
    return baker.make_recipe("todo")


@pytest.mark.django_db
def test_todo_list_create(api_client):
    # Test creating a Todo
    response = api_client.post("/todos/", {"content": "Test Todo"})
    assert response.status_code == 201
    assert Todo.objects.count() == 1


@pytest.mark.django_db
def test_todo_detail_retrieve(api_client, todo_baker):
    # Test retrieving a Todo
    response = api_client.get(f"/todos/{todo_baker.id}/")
    assert response.status_code == 200
    assert response.data["id"] == todo_baker.id


@pytest.mark.django_db
def test_todo_detail_update(api_client, todo_baker):
    # Test updating a Todo
    response = api_client.put(
        f"/todos/{todo_baker.id}/", {"content": "Updated Content", "status": 1}
    )
    assert response.status_code == 200
    assert Todo.objects.get(id=todo_baker.id).content == "Updated Content"


@pytest.mark.django_db
def test_todo_detail_delete(api_client, todo_baker):
    # Test deleting a Todo
    response = api_client.delete(f"/todos/{todo_baker.id}/")
    assert response.status_code == 204
    assert Todo.objects.count() == 0
