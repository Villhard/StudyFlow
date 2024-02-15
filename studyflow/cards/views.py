from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from .models import Card
from .serializers import CardSerializer


def index(request):
    return render(request, "index.html")


def view_cards(request):
    cards = Card.objects.all()
    context = {"cards": cards}
    return render(request, "cards/cards.html", context)


def view_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    context = {"card": card}
    return render(request, "cards/card.html", context)


# API
class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
