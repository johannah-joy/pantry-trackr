from django import forms
from django.contrib.auth.models import User
from pantry_trackr.models import *   # import user

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

