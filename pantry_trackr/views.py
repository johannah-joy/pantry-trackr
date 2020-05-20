# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm


# def home(request):
#     context = {
#         # 'posts': posts
#     }
#     return render(request, 'pantry_trackr/home.html', context)



# from django.shortcuts import render, redirect
# # from user.forms import UserForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# # Create your views here.

# # from django.shortcuts import render
# # from django.http import HttpResponse
# # from .models import User, PantryItem
# # # Create your views here.

# # def register(response):
# # 	return render(response, "pantry_trackr/register.html", {})

# # def pantry(response, id):
# #     items = ToDoList.objects.get(id=id)
# # 	return render(response, "pantry_trackr/my-pantry.html", {"ls":ls})

# # def addItem(response):
# #     return render(response, "pantry_trackr/add-item.html", {"form": form})

# '''
# def index(request):
#     return render(request,'pantry_trackr/index.html')
# '''
# def register(request):
#     # registered = False

#     # if the user is already signed in, we’ll redirect them away from the register page
#     if request.user.is_authenticated:
#         return redirect('/')
#     # if the request method is POST, that means that the form for creating a user has already been filled out and it’s time to create a user
#     if request.method == "POST":
#         # user_form = user_form(data=request.POST)
#         # construct the form object on the backend with the user-provided data
#         form = UserCreationForm(request.POST)
#         # if the form is valid, create the user and log them in, then send them to the main page
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         # else, dump them back on the user creation page with information about what data was invalid (ie, they requested a username already in use)
#         else:
#             return render(request, 'register.html', {'form': form})
#     # else, the user is accessing the page for the first time and should be met with the form for creating a new account
#     else:
#         return render(request, 'register.html', {'form': form})

# def login(request):
#     # if the user is already signed in, we’ll redirect them away from the sign-in page
#     if request.user.is_authenticated:
#         return render(request, 'my-pantry.html')
#     # if the request method is POST, the form for signing in has been filled and it’s time to authenticate the user to an account
#     if request.method == 'POST':
#         # authenticate the user with the user-provided data
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         # if the username and password correspond to an account, log the user in
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         # else, bring them back to the login page with their form information pre-filled
#         else:
#             form = AuthenticationForm(request.POST)
#             return render(request, 'login.html', {'form': form})
#     # else, the user is accessing the page for the first time and should be met with the form for logging in
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})

# def logout(request):
#     logout(request)
#     return redirect('/')


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


