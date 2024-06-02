from django.apps import AppConfig


class BasesettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaseSettings'
    verbose_name = "Базовые параметры"
