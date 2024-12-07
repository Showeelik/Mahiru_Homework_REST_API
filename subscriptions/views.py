from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Subscription
from courses.models import Course

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)
        subscription = Subscription.objects.filter(user=request.user, course=course)

        if subscription.exists():
            subscription.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=request.user, course=course)
            message = "Подписка добавлена"

        return Response({"message": message})
