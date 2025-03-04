"""App configuration for the F1 Django application."""

from django.apps import AppConfig


class F1Config(AppConfig):
    """Configuration class for the F1 application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'f1'
