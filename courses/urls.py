from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateView, LessonDetailView

# Создаем роутер для ViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    # Подключаем маршруты роутера
    path('', include(router.urls)),

    # Добавляем маршруты для Generic-классов
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
]
