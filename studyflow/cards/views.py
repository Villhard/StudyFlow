from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from .forms import CardForm
from .models import Card
from .serializers import CardSerializer


def index(request):
    return render(request, "index.html")


def cards(request):
    cards = Card.objects.all()
    context = {"cards": cards}
    return render(request, "cards/cards.html", context)


def card(request, pk=None):
    if pk:
        instance = get_object_or_404(Card, id=pk)
    else:
        instance = None

    form = CardForm(request.POST or None, instance=instance)
    context = {"form": form}

    if request.method == "POST" and form.is_valid():
        card = form.save(commit=False)
        card.user = request.user
        card.save()
        context.update({"form": form})

    return render(request, "cards/card.html", context)


# API
class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
