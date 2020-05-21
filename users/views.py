# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'vanilla/register.html', {'form': form})

class SignUpView(generic.CreateView):
    signup_form = UserCreationForm
    signup_template = 'signup.html'
    success_url = reverse_lazy('login')


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('my-pantry.html')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})