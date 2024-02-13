from cards.models import Card, Deck
from django import forms


class AddDeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = "__all__"


class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["front_side", "back_side", "deck", "user"]
        widgets = {
            "front_side": forms.Textarea(
                attrs={"rows": 3, "style": "resize: none"}
            ),
            "back_side": forms.Textarea(
                attrs={"rows": 3, "style": "resize: none"}
            ),
        }
