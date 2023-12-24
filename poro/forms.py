from django import forms
from .models import Poro


class PoroCreationForm(forms.Form):

    class Meta:
        model = Poro
        fields = ["name"]


class PoroEditForm(forms.Form):

    class Meta:
        model = Poro
        fields = ["name"]


class PoroDeleteForm(forms.Form):

    class Meta:
        model = Poro
        fields = ["hash_key", 'UUID']