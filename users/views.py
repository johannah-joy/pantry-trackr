from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# Create your views here.

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'vanilla/register.html', {'form': form})

def registration(request):
  context = {}
  context['form'] = RegistrationForm()
  return render(request, "register.html", context)