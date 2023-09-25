from rest_framework import mixins, viewsets
from .models import File
from .serializers import FileSerializer


# Create your views here.
class FileCreateViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Представление API для создания файлов.

    Класс FileCreateViewSet предоставляет возможность создавать новые файлы через API.
    Он использует CreateModelMixin для добавления функциональности создания модели File.

    Attributes:
        queryset: Запрос к модели File, начиная с пустого набора.
        serializer_class: Сериализатор для модели File.
    """

    queryset = File.objects.none()
    serializer_class = FileSerializer


class FileViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Представление API для просмотра файлов.

    Класс FileViewSet предоставляет возможность просматривать существующие файлы через API.
    Он использует ListModelMixin для добавления функциональности получения списка моделей File.

    Attributes:
        queryset: Запрос к модели File, начиная с всех доступных файлов.
        serializer_class: Сериализатор для модели File.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
