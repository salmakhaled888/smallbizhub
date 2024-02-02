from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductRatingViewSet

router = DefaultRouter()
router.register(r'rating', ProductRatingViewSet, basename='rating')


urlpatterns = [
    path('', include(router.urls)),
]