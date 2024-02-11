from django.urls import path

from .views import CardAPIView, view_card, view_cards, view_decks

urlpatterns = [
    path("decks/", view_decks, name="decks"),
    path("decks/<int:deck_id>/", view_cards, name="cards"),
    path("decks/<int:deck_id>/<int:card_id>/", view_card, name="card"),
]

# API
urlpatterns += [
    path("api/v1/cards/", CardAPIView.as_view(), name="api-v1-cards"),
]
