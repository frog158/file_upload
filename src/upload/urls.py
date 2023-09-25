from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileCreateViewSet, FileViewSet


# Создание маршрутизатора для представлений FileCreateViewSet и FileViewSet.
router = DefaultRouter()
# Регистрация маршрута "files" для FileViewSet.
router.register("files", FileViewSet, "files")
# Регистрация маршрута "upload" для FileCreateViewSet.
router.register("upload", FileCreateViewSet)

# Определение URL-шаблонов для API представлений.
urlpatterns = [
    # Включение маршрутов маршрутизатора в urlpatterns.
    path("", include(router.urls))
]
