from django.shortcuts import render
from rest_framework import generics

from .models import Card
from .serializers import CardSerializer


class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


def index(request):
    context = {"cards": Card.objects.all()}
    return render(request, "cards/index.html", context)
