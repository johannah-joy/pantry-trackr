from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from pantry_trackr.models import PantryItem
from django.contrib.auth import logout

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class HomeView(generic.DetailView):
    # model =
    template_name = 'home.html'
    # success_url = reverse_lazy('home')

    # def

        # return


class LoginView(generic.DetailView):
    # model =
    template_name = 'login.html'
    success_url = reverse_lazy('home')

#     # def

#         # return


# class AddItemView():
#     # model =
#     template_name = 'add-item.html'
#     # fields or success_url =

#     # def

#         # return


class MyPantryView(generic.DetailView):
    model = PantryItem
    template_name = 'my-pantry.html'
    # success_url = reverse_lazy('my-pantry')

    # def

        # return


# class UsedItemView():
#     # model =
#     template_name = 'used-item.html'
#     # fields or success_url =

#     # def

#         # return


# class ShoppingListView(generic.DetailView):
#     # model =
#     template_name = 'shopping-list.html'
#     # fields or success_url =

#     # def

#         # return


def logout_user(request):
    logout(request)
    # return HttpResponseRedirect(reverse('login.html'))
    return redirect('login.html')






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