from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from todo import views


def redirect_to_profile(request):
    return redirect("accounts/profile")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", views.ProfileView, name="profile"),
    path("", include("todo.urls")),
    path("api/", include("todo.api.urls", namespace="todo.api")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", redirect_to_profile, name="root_redirect"),
]
