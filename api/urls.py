from django.urls import path
from .views import PantryItemViewSet # UserRegisterViewSet
from rest_framework.routers import DefaultRouter


# router = routers.DefaultRouter()
router = DefaultRouter()
router.register('', PantryItemViewSet, basename='pantry-items')
# router.register('User', UserViewSet, basename='users')
# router.register('PantryItem', views.PantryItemViewSet, basename='pantry-items')

urlpatterns = router.urls