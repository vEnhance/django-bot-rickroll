"""Views for django-rickroll."""

from django.views.generic import RedirectView

from .settings import get_rickroll_url


class RickrollView(RedirectView):
    """Redirect to the rickroll URL."""

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """Return the rickroll URL from settings."""
        return get_rickroll_url()
