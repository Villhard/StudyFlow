from django import forms

from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["front_side", "back_side"]
        labels = {"front_side": "Front side", "back_side": "Back side"}
        widgets = {
            "front_side": forms.Textarea(attrs={"rows": 3}),
            "back_side": forms.Textarea(attrs={"rows": 3}),
        }
