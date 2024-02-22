from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cards/", views.cards, name="cards"),
    path("cards/add/", views.card, name="add"),
    path("card/<int:pk>/edit/", views.card, name="edit"),
    path("card/<int:pk>/delete/", views.card_delete, name="delete"),
    # API
    path("api/v1/cards/", views.CardAPIView.as_view(), name="api-v1-cards"),
]
