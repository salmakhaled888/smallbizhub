from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]