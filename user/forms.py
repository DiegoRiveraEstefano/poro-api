from django import forms


class UserGetTokenForm(forms.Form):

    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)