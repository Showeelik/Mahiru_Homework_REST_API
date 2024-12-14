from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Lesson
from .tasks import send_course_update_email
from .paginators import CoursePagination
from .permissions import IsModerator, IsOwner
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def perform_update(self, serializer):
        """
        Выполняет обновление курса и вызывает задачу для отправки писем
        """
        # Сохраняем обновленный курс
        course = serializer.save()

        # Получаем список подписчиков на курс
        subscribers = course.subscriptions.all()  # Связь через ForeignKey или ManyToMany
        for subscriber in subscribers:
            # Запускаем задачу для отправки писем
            send_course_update_email.delay(subscriber.user.email, course.name)

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
