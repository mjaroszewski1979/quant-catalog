# Import AppConfig class from Django for configuring application settings
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """
    Configuration class for the Catalog application.
    Inherits from Django's AppConfig to set application-specific configurations.
    """

    # Specifies the default field type for auto-incrementing primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Defines the name of the application, which is used by Django to identify the app
    name = 'catalog'
