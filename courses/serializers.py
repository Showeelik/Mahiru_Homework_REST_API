from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "preview", "video_url"]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # Include nested lessons
    lesson_count = serializers.SerializerMethodField()  # Computed field

    class Meta:
        model = Course
        fields = ["id", "name", "preview", "description", "lesson_count", "lessons"]  # Ensure all fields are included

    def get_lesson_count(self, obj):
        return obj.lessons.count()
