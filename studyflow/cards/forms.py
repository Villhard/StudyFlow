from django import forms


class AddDeckForm(forms.Form):
    name = forms.CharField(max_length=255)


class AddCardForm(forms.Form):
    front_side = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "style": "resize:none;"})
    )
    back_side = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "style": "resize:none;"})
    )
