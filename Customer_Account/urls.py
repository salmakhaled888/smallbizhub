from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerAccountViewSet

router = DefaultRouter()
router.register(r'customer', CustomerAccountViewSet, basename='customer')


urlpatterns = [
    path('', include(router.urls)),
]