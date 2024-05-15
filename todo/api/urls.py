from django.urls import path

from .views import TodoDetail, TodoListCreate

app_name = "todo"
urlpatterns = [
    path("todos/", TodoListCreate.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TodoDetail.as_view(), name="todo-detail"),
]
