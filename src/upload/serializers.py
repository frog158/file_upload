from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели File.

    Позволяет преобразовать объекты модели File в формат JSON и наоборот.

    Attributes:
        Meta (class): Вложенный класс, определяющий метаданные сериализатора.
            - model: Связанная модель, которая будет сериализована.
            - fields: Список полей модели, которые будут включены в сериализацию (все поля).
            - extra_kwargs: Дополнительные настройки для полей модели.
                - processed: Устанавливает поле 'processed' как только для чтения.
                - uploaded_at: Устанавливает поле 'uploaded_at' как только для чтения.
    """

    class Meta:
        model = File
        fields = "__all__"
        extra_kwargs = {
            "processed": {"read_only": True},
            "uploaded_at": {"read_only": True},
        }
