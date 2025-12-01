"""URL configuration for tests."""

from django.urls import include, path

urlpatterns = [
    path("", include("django_rickroll.urls")),
]
