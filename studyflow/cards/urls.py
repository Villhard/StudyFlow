from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cards/", views.CardListView.as_view(), name="cards"),
    path("cards/add/", views.CardCreateView.as_view(), name="add"),
    path("cards/<int:pk>/edit/", views.CardUpdateView.as_view(), name="edit"),
    path("cards/<int:pk>/delete/", views.CardDeleteView.as_view(), name="delete"),
]
