from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import generics

from .forms import CardForm
from .models import Card
from .serializers import CardSerializer


def index(request):
    return render(request, "index.html")


class CardListView(ListView):
    model = Card
    template_name = "cards/cards.html"
    context_object_name = "cards"
    paginate_by = 12


class CardMixin:
    model = Card
    form_class = CardForm
    success_url = "/cards/"


class CardCreateView(CardMixin, CreateView):
    pass

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardUpdateView(CardMixin, UpdateView):
    pass


class CardDeleteView(DeleteView):
    model = Card
    success_url = "/cards/"


# API
class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
