from django.urls import path

from .views import CardAPIView, index

urlpatterns = [
    path("", index, name="index"),
    path("api/v1/cards/", CardAPIView.as_view(), name="api-v1-cards"),
]
