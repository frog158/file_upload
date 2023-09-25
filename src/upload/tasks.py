import os
from celery import shared_task
from . import models, utils


# Задача Celery для обработки файла.
@shared_task
def process_file(file_id):
    """
    Асинхронная задача для обработки файла.

    Args:
        file_id (int): Идентификатор файла, который нужно обработать.

    Процедура обработки файла зависит от его расширения, и соответствующая
    функция из модуля utils вызывается для обработки файла.

    Если файл отсутствует или его обработка завершилась успешно, функция завершается.

    """
    file = models.File.objects.get(id=file_id)
    if not file.file:
        return
    helper_dict = {
        "jpeg": utils.process_jpeg,
        "png": utils.process_png,
        "webp": utils.process_webp,
        "txt": utils.process_txt,
    }
    _, extension = os.path.splitext(file.file.name)

    helper_dict.get(extension[1:], utils.process)(file)
