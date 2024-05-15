from django.urls import path

from .views import TodoView

urlpatterns = [
    path("dashboard/", TodoView, name="todo"),
]
