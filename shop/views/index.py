from django.shortcuts import render

from shop.models import Category, Subcategory, Product


def index(request):
    # The homepage of app
    categories = Category.objects.count()
    subcategories = Subcategory.objects.count()
    products = Product.objects.count()
    context = {'categories':categories, 'subcategories':subcategories, 'products':products}
    return render(request, "shop/index.html", context)
