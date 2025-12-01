"""pytest configuration for bot-rickroll tests."""

import django
from django.conf import settings


def pytest_configure():
    """Configure Django settings for tests."""
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
        ],
        ROOT_URLCONF="tests.urls",
        SECRET_KEY="test-secret-key-not-for-production",
    )
    django.setup()
