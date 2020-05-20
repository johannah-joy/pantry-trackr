# manually added this

from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'pantry_trackr'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
# home and about are from VIEWS in this app folder AND templates folder is in this app folder