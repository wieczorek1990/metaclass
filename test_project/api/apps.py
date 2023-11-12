from django import apps


class ApiConfig(apps.AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
