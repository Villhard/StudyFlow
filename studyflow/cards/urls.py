from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("cards/", views.cards, name="cards"),
    path("card/", views.card, name="add-card"),
    path("card/<int:pk>", views.card, name="edit-card"),
    # API
    path("api/v1/cards/", views.CardAPIView.as_view(), name="api-v1-cards"),
]
