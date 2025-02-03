from rest_framework import serializers

from subscriptions.models import Subscription

from .models import Course, Lesson
from .validators import youtube_url_validator


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[youtube_url_validator])

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "preview", "video_url", "course"]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "preview", "lessons", "lesson_count", "is_subscribed"]

    def get_is_subscribed(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    def get_lesson_count(self, obj):
        return obj.lessons.count()
