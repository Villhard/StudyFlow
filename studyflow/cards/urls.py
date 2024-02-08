from cards.views import CardAPIView
from django.urls import path

urlpatterns = [
    path("api/v1/cards/", CardAPIView.as_view()),
]
