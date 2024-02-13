from cards.models import Card
from django import forms


class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["front_side", "back_side", "user"]
        widgets = {
            "front_side": forms.Textarea(
                attrs={"rows": 3, "style": "resize: none"}
            ),
            "back_side": forms.Textarea(
                attrs={"rows": 3, "style": "resize: none"}
            ),
        }
