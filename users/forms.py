from django import forms
from pantry_trackr.models import *

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput())