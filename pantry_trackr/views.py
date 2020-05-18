from django.shortcuts import render
from user.forms import UserForm

# Create your views here.

def index(request):
    return render(request,'pantry_trackr/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = user_form(data=request.POST)