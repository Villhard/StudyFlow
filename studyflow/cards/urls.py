from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cards/", views.CardListView.as_view(), name="cards"),
    path("cards/add/", views.CardCreateView.as_view(), name="add"),
    path("card/<int:pk>/edit/", views.CardUpdateView.as_view(), name="edit"),
    path(
        "card/<int:pk>/delete/", views.CardDeleteView.as_view(), name="delete"
    ),
    # API
    path("api/v1/cards/", views.CardAPIView.as_view(), name="api-v1-cards"),
]
