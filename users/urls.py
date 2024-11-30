from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserCreateAPIView, CustomTokenObtainPairView, PaymentListView

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payment-list"),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
