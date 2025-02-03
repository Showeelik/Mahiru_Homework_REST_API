from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from courses.models import Course

from .models import Payment, User
from .serializers import PrivateUserSerializer, PublicUserSerializer, UserPaymentSerializer, UserSerializer
from .services.stripe_service import (create_checkout_session, create_stripe_price, create_stripe_product,
                                      get_payment_status)


class CreatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        product_id = create_stripe_product(course)
        price_id = create_stripe_price(product_id, course.price)
        success_url = "http://127.0.0.1:8000/success/"
        cancel_url = "http://127.0.0.1:8000/cancel/"
        payment_url = create_checkout_session(price_id, success_url, cancel_url)

        return Response({"payment_url": payment_url})


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = UserPaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "method", "created_at"]
    ordering_fields = ["created_at"]


class PaymentStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        status = get_payment_status(session_id)
        return Response({"status": status})


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class ProfileViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if user == request.user:
            serializer = PrivateUserSerializer(user)
        else:
            serializer = PublicUserSerializer(user)
        return Response(serializer.data)
