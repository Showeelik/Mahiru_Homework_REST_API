from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .models import Payment
from .serializers import UserPaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = UserPaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]  # Поля для фильтрации
    ordering_fields = ["date"]  # Поля для сортировки
