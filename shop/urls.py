from django.conf.urls import url

from shop.models import Product
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Urls for categories
    url(r'^categories$', views.categories, name='categories'),
    url(r'^categories/all$', views.categories_all, name='categories_all'),
    url(r'^categories/add$', views.categories_add, name='categories_add'),
    url(r'^categories/delete$', views.categories_delete, name='categories_delete'),
    url(r'^categories/edit$', views.categories_edit, name='categories_edit'),

    # Urls for subcategories
    url(r'^subcategories$', views.subcategories, name='subcategories'),
    url(r'^subcategories/all$', views.subcategories_all, name='subcategories_all'),
    url(r'^subcategories/add$', views.subcategories_add, name='subcategories_add'),
    url(r'^subcategories/delete$', views.subcategories_delete, name='subcategories_delete'),
    url(r'^subcategories/edit$', views.subcategories_edit, name='subcategories_edit'),


    #Urls for products
    url(r'^products/$', views.IndexView.as_view(), name='products'),
    url(r'^products/add$', views.ProductCreate.as_view(), name='add_product'),

    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='update_product'),

    url(r'^products/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='delete_product'),


]