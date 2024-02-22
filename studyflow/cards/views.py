from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
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
    template_name = "cards/card.html"
    success_url = "/cards/"


class CardCreateView(CardMixin, CreateView):
    pass

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardUpdateView(CardMixin, UpdateView):
    pass


def card_delete(request, pk):
    instance = get_object_or_404(Card, id=pk)
    form = CardForm(instance=instance)
    context = {"form": form}
    if request.method == "POST":
        instance.delete()
        return redirect("cards")
    return render(request, "cards/card.html", context)


# API
class CardAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
