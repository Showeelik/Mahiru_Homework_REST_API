from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, PaymentListView, UserCreateAPIView, CreatePaymentView, PaymentStatusView

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payment-list"),
    path("payments/<int:course_id>/", CreatePaymentView.as_view(), name="create-payment"),
    path("payment-status/<str:session_id>/", PaymentStatusView.as_view(), name="payment-status"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
