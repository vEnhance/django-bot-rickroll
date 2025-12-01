"""Tests for django-rickroll URL patterns."""

import pytest
from django.test import Client

from django_rickroll.settings import DEFAULT_RICKROLL_URL


@pytest.fixture
def client():
    """Return a Django test client."""
    return Client()


class TestWordPressPaths:
    """Test WordPress-related paths are rickrolled."""

    @pytest.mark.parametrize(
        "path",
        [
            "/wp-admin/",
            "/wp-admin/index.php",
            "/wp-content/",
            "/wp-content/plugins/something",
            "/wp-includes/",
            "/wp-includes/js/jquery.js",
            "/wp-json/",
            "/wp-json/wp/v2/posts",
            "/wordpress/",
            "/wp/",
        ],
    )
    def test_wordpress_paths_redirect(self, client, path):
        """WordPress paths should redirect to rickroll URL."""
        response = client.get(path)
        assert response.status_code == 302
        assert response.url == DEFAULT_RICKROLL_URL


class TestPHPPaths:
    """Test PHP-related paths are rickrolled."""

    @pytest.mark.parametrize(
        "path",
        [
            "/xmlrpc.php",
            "/shell.php",
            "/cmd.php",
            "/c99.php",
            "/r57.php",
            "/eval-stdin.php",
            "/test.php",
            "/info.php",
            "/phpinfo.php",
            "/random-file.php",
            "/deeply/nested/path/file.php",
        ],
    )
    def test_php_paths_redirect(self, client, path):
        """PHP file paths should redirect to rickroll URL."""
        response = client.get(path)
        assert response.status_code == 302
        assert response.url == DEFAULT_RICKROLL_URL


class TestAdminPaths:
    """Test admin and CMS paths are rickrolled."""

    @pytest.mark.parametrize(
        "path",
        [
            "/administrator/",
            "/phpmyadmin/",
            "/phpMyAdmin/",
            "/pma/",
            "/mysql/",
            "/cpanel/",
            "/joomla/",
            "/drupal/",
            "/magento/",
        ],
    )
    def test_admin_paths_redirect(self, client, path):
        """Admin and CMS paths should redirect to rickroll URL."""
        response = client.get(path)
        assert response.status_code == 302
        assert response.url == DEFAULT_RICKROLL_URL


class TestSensitivePaths:
    """Test sensitive file paths are rickrolled."""

    @pytest.mark.parametrize(
        "path",
        [
            "/.env",
            "/.git/",
            "/.git/config",
            "/.svn/",
            "/.htaccess",
            "/.htpasswd",
            "/.well-known/",
            "/.well-known/security.txt",
            "/config/",
            "/backup/",
            "/backups/",
        ],
    )
    def test_sensitive_paths_redirect(self, client, path):
        """Sensitive file paths should redirect to rickroll URL."""
        response = client.get(path)
        assert response.status_code == 302
        assert response.url == DEFAULT_RICKROLL_URL


class TestUploadPaths:
    """Test upload and file manager paths are rickrolled."""

    @pytest.mark.parametrize(
        "path",
        [
            "/upload/",
            "/uploads/",
            "/files/",
            "/file-manager/",
            "/filemanager/",
            "/elfinder/",
            "/vendor/",
            "/public/",
            "/modules/",
        ],
    )
    def test_upload_paths_redirect(self, client, path):
        """Upload and file paths should redirect to rickroll URL."""
        response = client.get(path)
        assert response.status_code == 302
        assert response.url == DEFAULT_RICKROLL_URL


class TestCustomRickrollUrl:
    """Test custom rickroll URL configuration."""

    def test_custom_url(self, client, settings):
        """Custom RICKROLL_URL setting should be used."""
        custom_url = "https://example.com/custom-rickroll"
        settings.RICKROLL_URL = custom_url

        response = client.get("/wp-admin/")
        assert response.status_code == 302
        assert response.url == custom_url
