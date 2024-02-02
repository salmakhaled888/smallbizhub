from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderDetailsViewSet

router = DefaultRouter()
router.register(r'orderdetails', OrderDetailsViewSet, basename='OrderDetails')


urlpatterns = [
    path('', include(router.urls)),
]