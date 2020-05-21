# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from pantry_trackr.models import *   # import user
'''
class UserCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
'''

# class UserRegisterForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ["username", "password1", "password2"]