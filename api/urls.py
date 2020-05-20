from django.urls import path
from .views import UserViewSet, PantryItemViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', UserViewSet, basename='users')
router.register('', PantryItemViewSet, basename='pantry-items')
# router.register('User', UserViewSet, basename='users')
# router.register('PantryItem', PantryItemViewSet, basename='pantry-items')

urlpatterns = router.urls