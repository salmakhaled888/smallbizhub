from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SellerAccountViewSet

router = DefaultRouter()
router.register(r'seller', SellerAccountViewSet, basename='seller')


urlpatterns = [
    path('', include(router.urls)),
]