from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.db.models import Q
from .models import (
    Product,
    ProductInventory,
    Category,
    Media
)

# FOR PRACTISE BUT IMAGES DOESNT WORK
def get_fake(request):
    products = Media.objects.select_related("product_inventory__product").filter(is_feature = True).values(
        "image", "alt_text","product_inventory__sale_price", "product_inventory__product__id", "product_inventory__product__name", "product_inventory__product__slug"
    )
    context = {
        "products": products
    }
    return render(request, 'inventory/fake.html', context)
# 


# Create your views here.

# 404 PAGE
def handler404(request, exception):
    return render(request, '404.html', status=404)
# END 404 PAGE

# 500 SERVER ERROR
def server_error(request):
    return render(request, '500.html', status=500)
# END 500 SERVER ERROR



# SEARCH FUNCTION
def search(q = None):
    query = (
        Q(product__name__icontains = q) |
        Q(brand__name__icontains = q) |
        Q(sale_price__icontains = q)
    )
    datas = ProductInventory.objects.filter(query).select_related("product")

    if len(datas) == 0:
        return 0
    return datas
# END SEARCH FUNCTION

# ALL PRODUCTS
def products(request):
    q = request.GET.get('q') or None
    if q == None:
        products = ProductInventory.objects.select_related("product")
    else:
        products = search(q)
        if products == 0:
            messages.warning(request, 'Product does not exists!')
            return redirect('inventory:list-products')
    context = {
        'products': products
    }
    return render(request, 'inventory/products.html', context)
# END ALL PRODUCTS


# PRODUCTS BY CATEGORY
def products_by_category(request, slug):
    #slug = "biznes-kitaplar"
    category = get_object_or_404(Category, slug = slug) 
    products = ProductInventory.objects.filter(
        product__category__in = Category.objects.get(slug=slug).get_descendants(include_self = True)
    )
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'inventory/products_by_category.html', context)
# END PRODUCTS BY CATEGORY


# PRODUCT BY CATEGORY CHILDREN
def products_by_category_children(request, slug):
    category = get_object_or_404(Category, slug = slug)
    products = ProductInventory.objects.filter(
        product__category__in = Category.objects.get(slug=slug).get_descendants(include_self = True)
    )
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'inventory/filtered_category_for_products.html', context)
# END PRODUCT BY CATEGORY CHILDREN


# PRODUCT DETAIL
def product_detail(request, slug):
    product = get_object_or_404(ProductInventory.objects.select_related("product", "brand"), product__slug = slug)
    context = {
        'product': product
    }
    return render(request, 'inventory/product_detail.html', context)
# END PRODUCT DETAIL