"""small_biz_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Customer_Account.urls')),
    path('api/', include('Seller_Account.urls')),
    path('api/', include('User.urls')),
    path('api/',include('Cart_Items.urls')),
    path('api/', include('Order_Details.urls')),
    path('api/', include('Order_Items.urls')),
    path('api/', include('Product.urls')),
    path('api/', include('Product_Rating.urls')),
    path('api/', include('Product_Category.urls')),
    path('api/', include('Seller_Shop.urls')),
    path('api/', include('BusinessBankAccount.urls')),
    path('api/', include('ShopCategory.urls')),
    path('api/', include('BusinessType.urls')),
    path('api/', include('User_IsCustomer.urls')),
    path('api/', include('Login.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
