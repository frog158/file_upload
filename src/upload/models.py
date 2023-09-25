from django.db import models
from django.core.validators import FileExtensionValidator
from . import validators


MAX_FILE_SIZE = 2 * 2**20  # Максимальный размер файла - 2 мегабайта


# Create your models here.
class File(models.Model):
    """
    Модель для хранения файлов.

    Attributes:
        file (FileField): Поле для хранения файла с применением нескольких валидаторов.
            - MaxFileSizeValidator: Валидатор для ограничения размера файла.
            - FileExtensionValidator: Валидатор для разрешенных расширений файлов (png, jpeg, webp, txt).
        uploaded_at (DateTimeField): Дата и время загрузки файла.
        processed (BooleanField): Флаг для отслеживания обработки файла.
    """

    file = models.FileField(
        validators=[
            validators.MaxFileSizeValidator(MAX_FILE_SIZE),
            FileExtensionValidator(
                allowed_extensions=["png", "jpeg", "webp", "txt"]
            ),
        ]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
