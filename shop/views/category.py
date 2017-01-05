from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from shop.models import Category
from shop.models import Subcategory
import json




def categories(request):
    #Show the categories page
    return render(request, "shop/categories.html")

def categories_all(request):
    #get all categories (For angular)
    categories = serializers.serialize('json', Category.objects.all())
    return HttpResponse(categories, content_type='json')

def categories_add(request):
    #Submit the add new category
    data = json.loads(request.body)
    category = Category()
    category.name = data['name']
    category.save()

    #Get inserted ID
    last = Category.objects.latest('id')
    return JsonResponse({'code': "200", "id": last.pk, "name" : data['name']})

def categories_edit(request):
    #Submit the edit category
    data = json.loads(request.body)
    category = Category.objects.get(pk=data['id'])
    category.name = data['name']
    category.save()
    return JsonResponse({'code': "200", "id": data['id'], "name": data['name']})

def categories_delete(request):
    data = json.loads(request.body)
    Category.objects.filter(pk=data['id']).delete()
    return JsonResponse({'code': "200"})
