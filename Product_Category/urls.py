from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductCategoryViewSet

router = DefaultRouter()
router.register(r'productcategory', ProductCategoryViewSet, basename='productcategory')


urlpatterns = [
    path('', include(router.urls)),
]