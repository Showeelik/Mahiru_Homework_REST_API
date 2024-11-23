from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    """
    ViewSet для CRUD операций над курсами.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateView(ListCreateAPIView):
    """
    Представление для получения списка и создания уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления урока.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
