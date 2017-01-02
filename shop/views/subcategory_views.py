from django.shortcuts import render
from shop.models import Subcategory
def subcategories(request):
    data = Subcategory.objects.all()
    context = {'subcategories': data}
    return render(request, "shop/subcategories.html", context)
