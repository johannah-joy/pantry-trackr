from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from pantry_trackr.models import PantryItem
from .forms import PantryItemForm
from django.views.generic.edit import FormView
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



# class AddItemView(generic.FormView):
#     form_class = PantryForm
#     template_name = 'add-item.html'
#     success_url = reverse_lazy('my-pantry')

# class AddItemView(generic.CreateView):
#     # model = PantryItem
#     form_class = PantryItem
#     # template_name = 'add-item.html'
#     template_name = 'my-pantry.html'
#     # success_url = reverse_lazy('my-pantry')

#     # def
#         # return


# def addItem(request):
#     pantry = PantryItem.objects.all()
#     # item_name = request.POST['item_name']
#     # quantity_min = request.POST['quantity_min']
#     # quantity_now = request.POST['quantity_now']
#     # return HttpResponseRedirect(reverse('users:my-pantry'))
#     return render(request, 'add-item.html', {'pantry': pantry})

# def addItem(request):
#     form = PantryItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form.PantryItemForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'add-item.html', context)

def addItem(request): 
    if request.method == 'POST':
        form = PantryItemForm(request.POST or None) 
        if form.is_valid(): 
            form.save()
            pantry = PantryItem.objects.all()
            return render(request, 'my-pantry.html', {'pantry': pantry})
    else:
        form_class = PantryItemForm
    return render(request, "add-item.html", {
        'form': form_class,})



# class MyPantryView(generic.CreateView):
#     model = PantryItem
#     template_name = 'my-pantry.html'
#     # fields = ['item_now', 'quantity_min', 'quantity_now']
#     success_url = reverse_lazy('my-pantry')

    # def
        # return

def myPantry(request):
    PantryItem.objects.create(item_name=request.POST['item_name'], quantity_min=request.POST['quantity_min'], quantity_now=request.POST['quantity_now'])
    return HttpResponseRedirect(reverse('users:my-pantry'))


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