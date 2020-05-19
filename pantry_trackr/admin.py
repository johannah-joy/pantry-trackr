from django.contrib import admin

# Register your models here.

from .models import User, PantryItem  # import ALL MODELS

admin.site.register(User)
admin.site.register(PantryItem)