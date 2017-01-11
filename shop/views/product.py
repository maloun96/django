from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views import generic
from django.shortcuts import render
from shop.models import  Product
from shop.models import Subcategory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import json
from shop.forms import ProductForm
from django.contrib.auth.decorators import login_required



class IndexView(generic.ListView):
    template_name = 'shop/products.html'
    context_object_name = 'data'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreate(CreateView):
    model = Product
    # fields = ['name', 'price', 'subcategory', 'image']
    success_url = reverse_lazy('add_product')
    success_message = 'Success'
    form_class = ProductForm


class ProductUpdate(UpdateView):
    model = Product
    # fields = ['name', 'price', 'subcategory', 'image']
    success_url = reverse_lazy('products')
    success_message = 'Success'
    form_class = ProductForm

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
    form_class = ProductForm

