from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

app_name = 'inventory'



urlpatterns = [
    path('', views.products, name = 'list-products'),
    path('list/', views.get_fake),
    path('products/<slug:slug>/', views.products_by_category, name = 'products-by-category'),
    path('product_detail/<slug:slug>/', views.product_detail, name = 'product-detail'),
    path('category-child/<slug:slug>/', views.products_by_category_children, name = 'category-child'),


]
handler404 = 'inventory.views.handler404'
handler500 = 'inventory.views.server_error'