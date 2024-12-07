from django.urls import path
from .views import SubscriptionView

urlpatterns = [
    # Другие маршруты
    path("", SubscriptionView.as_view(), name="subscriptions"),
]