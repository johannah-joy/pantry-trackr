# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'vanilla/register.html', {'form': form})

# def registration(request):
#   context = {}
#   context['form'] = RegistrationForm()
#   return render(request, "register.html", context)

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


'''
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
'''