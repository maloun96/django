from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from shop.models import Category
from shop.models import Subcategory
import json

def subcategories(request):
    #Show the categories page
    #Get all categories for form
    categories = Category.objects.all()
    context = {'categories' : categories}
    return render(request, "shop/subcategories.html", context)

def subcategories_all(request):
    #get all subcategories (For angular)
    c = Subcategory.objects.all()

    list = []
    for row in c:
        list.append({'subcategory_name': row.name, 'subcategory_id': row.id, 'category_name': row.category.name, 'category_id' : row.category.id})

    list= json.dumps(list)

    return HttpResponse(list, content_type='json')

def subcategories_add(request):
    #Submit the add new category
    data = json.loads(request.body)
    category = Category.objects.filter(pk=data['category']).first()

    subcategory = Subcategory()
    subcategory.name = data['name']
    subcategory.category = category
    subcategory.save()

    #Get inserted ID
    last = Subcategory.objects.latest('id')

    last = {'subcategory_name': last.name, 'subcategory_id': last.id, 'category_name': last.category.name, 'category_id' : last.category.id};
    return JsonResponse({'code': "200", "obj" : last})

def subcategories_edit(request):
    #Submit the edit category
    data = json.loads(request.body)
    category = Category.objects.get(pk=data['category_id'])
    subcategory = Subcategory.objects.get(pk=data['subcategory_id'])
    subcategory.name = data['name']
    subcategory.category = category
    subcategory.save()

    # Get inserted ID
    last = Subcategory.objects.filter(pk=subcategory.id).first()
    return JsonResponse({'code': "200", 'subcategory_name': last.name, 'subcategory_id': last.id, 'category_name': last.category.name, 'category_id': last.category.id })

def subcategories_delete(request):
    data = json.loads(request.body)
    Subcategory.objects.filter(pk=data['id']).delete()
    return JsonResponse({'code': "200"})
