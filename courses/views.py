from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Lesson
from .permissions import IsModerator, IsOwner
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.request.user.courses.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update"]:
            return [IsModerator()]
        return [IsOwner()]


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
