from django.apps import AppConfig


# Конфигурация приложения "upload".
class UploadConfig(AppConfig):
    # Использование большого авто-поля для автоматического
    # выбора типа поля в базе данных.
    default_auto_field = "django.db.models.BigAutoField"
    # Имя приложения.
    name = "upload"

    # Метод ready, который будет выполнен при загрузке приложения.
    def ready(self):
        # Импорт сигналов при загрузке приложения.
        from . import signals  # noqa
