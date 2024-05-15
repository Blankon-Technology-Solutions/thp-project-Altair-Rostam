from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("todo.urls")),
    path("api/", include("todo.api.urls", namespace="todo.api")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
