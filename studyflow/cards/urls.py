from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("decks/", views.view_decks, name="decks"),
    path("decks/<int:deck_id>/", views.view_cards, name="cards"),
    path("decks/add_deck/", views.add_deck, name="add_deck"),
    path("decks/<int:deck_id>/<int:card_id>/", views.view_card, name="card"),
    path("decks/add_card", views.add_card, name="add_card"),
]

# API
urlpatterns += [
    path("api/v1/cards/", views.CardAPIView.as_view(), name="api-v1-cards"),
]
