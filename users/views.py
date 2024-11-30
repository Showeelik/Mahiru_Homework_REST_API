from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Payment, User
from .serializers import PrivateUserSerializer, PublicUserSerializer, UserPaymentSerializer, UserSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = UserPaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]  # Поля для фильтрации
    ordering_fields = ["date"]  # Поля для сортировки


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