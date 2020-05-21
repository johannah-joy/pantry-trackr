from django.contrib import admin

# Register/IMPORT your models here.

from .models import PantryItem  # UserRegister

# admin.site.register(UserRegister)
admin.site.register(PantryItem)