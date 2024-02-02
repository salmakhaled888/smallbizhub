from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SellerShopViewSet

router = DefaultRouter()
router.register(r'sellershop', SellerShopViewSet, basename='sellershop')


urlpatterns = [
    path('', include(router.urls)),
]