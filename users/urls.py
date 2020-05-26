from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('home/', views.HomeView.as_view(), name='home'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('add-item/', views.AddItemView.as_view(), name='add-item'),
    # path('my-pantry/', views.MyPantryView.as_view(), name='my-pantry'),
    # path('used-item/', views.UsedItemView.as_view(), name='used-item'),
    # path('shopping-list/', views.ShoppingListView.as_view(), name='shopping-list'),
]
