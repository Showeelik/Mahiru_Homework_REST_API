from rest_framework import serializers
from .models import User, Payment


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['date', 'amount', 'payment_method', 'course', 'lesson']

class UserProfileSerializer(serializers.ModelSerializer):
    payments = UserPaymentSerializer(many=True, read_only=True, source='payments')

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']