"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('inventory.urls', namespace='inventory')),
    path('basket/', include('basket.urls', namespace="basket")),
    path('account/', include('account.urls', namespace="account")),
    path('payment/', include('payment.urls', namespace="payment")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('wishlist/', include('wishlist.urls', namespace="wishlist")),
    path('checkout/', include('checkout.urls', namespace="checkout")),
    
    # API
    path("api/", include("api.urls", namespace="api")),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

