from rest_framework import serializers

from .models import Payment, User


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["date", "amount", "payment_method", "course", "lesson"]

class UserProfileSerializer(serializers.ModelSerializer):
    payments = UserPaymentSerializer(many=True, read_only=True, source="payments")

    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar", "payments"]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone', 'city', 'avatar']

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает обычного пользователя с email."""
        if not email:
            raise ValueError('Email обязателен для создания пользователя')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'city']

class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'