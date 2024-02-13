from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("cards/", views.view_cards, name="cards"),
    path("cards/<int:card_id>", views.view_card, name="card"),
    path("cards/add_card/", views.add_card, name="add-card"),
]

# API
urlpatterns += [
    path("api/v1/cards/", views.CardAPIView.as_view(), name="api-v1-cards"),
]
