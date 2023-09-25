from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValidator:
    """
    Валидатор для ограничения размера загружаемого файла.

    Ограничивает размер загружаемого файла максимальным значением 'max_size'.
    Если размер файла превышает указанный лимит, вызывается исключение ValidationError
    с пользовательским сообщением.

    Args:
        max_size (int): Максимальный размер файла в байтах.
        message (str, optional): Пользовательское сообщение об ошибке. По умолчанию,
            генерируется стандартное сообщение.

    Attributes:
        message (str): Шаблон сообщения об ошибке. Содержит местозаполнители {size} и {max_size},
            которые будут заменены на фактический размер файла и максимальный размер соответственно.

    Usage:
        max_size_validator = MaxFileSizeValidator(max_size=1024*1024)  # Ограничение до 1 МБ.
    """

    message = (
        "Файл {size} слишком большой." "Максимальный размер файла {max_size}"
    )

    def __init__(self, max_size, message=None):
        self.max_size = max_size
        self.message = message or self.message

    def __call__(self, value):
        """
        Проверяет размер загружаемого файла и вызывает исключение ValidationError при превышении лимита.

        Args:
            value (File): Загружаемый файл.

        Raises:
            ValidationError: Если размер файла превышает максимально допустимый лимит.
        """
        if value.size > self.max_size:
            raise ValidationError(
                self.message.format(
                    size=filesizeformat(value.size),
                    max_size=filesizeformat(self.max_size),
                )
            )
