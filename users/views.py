# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'vanilla/register.html', {'form': form})

class SignUpView(generic.CreateView):
    signup_form = UserCreationForm
    signup_template = 'signup.html'
    success_url = reverse_lazy('login')


class HomeView():
    # model =
    template_name = 'home.html'
    # fields or success_url =

    # def

        # return


class LoginView():
    # model =
    template_name = 'login.html'
    # fields or success_url =

    # def

        # return


class AddItemView():
    # model =
    template_name = 'add-item.html'
    # fields or success_url =

    # def

        # return


class MyPantryView():
    # model =
    template_name = 'my-pantry.html'
    # fields or success_url =

    # def

        # return


class UsedItemView():
    # model =
    template_name = 'used-item.html'
    # fields or success_url =

    # def

        # return


class ShoppingListView():
    # model =
    template_name = 'shopping-list.html'
    # fields or success_url =

    # def

        # return




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