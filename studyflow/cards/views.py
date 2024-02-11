from django.shortcuts import render
from rest_framework import generics

from .models import Card, Deck
from .serializers import CardSerializer


class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


def view_decks(request):
    context = {"decks": Deck.objects.all()}
    return render(request, "cards/decks.html", context)


def view_cards(request, deck_id):
    context = {"cards": Card.objects.filter(deck=deck_id)}
    return render(request, "cards/cards.html", context)


def view_card(request, deck_id, card_id):
    context = {"card": Card.objects.get(id=card_id)}
    return render(request, "cards/card.html", context)
