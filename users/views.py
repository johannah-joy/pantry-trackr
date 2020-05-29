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


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class LoginView(generic.DetailView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class AddItemView(generic.CreateView):
    model = PantryItem
    # template_name = 'add-item.html'
    template_name = 'my-pantry.html'
    success_url = reverse_lazy('my-pantry')

#     # def

#         # return


# def addItem(request):
#     return HttpResponseRedirect('/my-pantry/')


class MyPantryView(generic.CreateView):
    model = PantryItem
    template_name = 'my-pantry.html'
    fields = ['item_now', 'quantity_min', 'quantity_now']
    success_url = reverse_lazy('my-pantry')

    # # ADD ITEM and USED AN ITEM will be in this view also

    # def

        # return


class UsedItemView(generic.UpdateView):
    model = PantryItem
    # template_name = 'used-item.html'
    template_name = 'my-pantry.html'
    success_url = reverse_lazy('my-pantry')

#     # def

#         # return


# class ShoppingListView(generic.DetailView):
#     # model =
#     template_name = 'shopping-list.html'
#     # fields or success_url =

#     # def

#         # return


def logout_view(request):
    logout(request)
    return redirect('login')