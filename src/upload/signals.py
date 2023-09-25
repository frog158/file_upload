from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from . import models, tasks


# Декоратор receiver используется для привязки функции к сигналу post_save модели File.
@receiver(post_save, sender=models.File)
def process_file(instance, created, **kwargs):
    """
    Обработчик сигнала post_save для модели File.

    При создании или обновлении объекта модели File, эта функция проверяет, не был ли
    файл уже обработан, и если нет, запускает асинхронную задачу process_file.delay()
    для обработки файла.

    Args:
        instance (File): Экземпляр модели File, который был сохранен.
        created (bool): Флаг, указывающий, был ли объект только что создан.
        **kwargs: Дополнительные аргументы.
    """
    if not instance.processed:
        transaction.on_commit(lambda: tasks.process_file.delay(instance.id))
