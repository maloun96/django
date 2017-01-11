from django.conf.urls import url

from shop.models import Product
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),

    url(r'^register/$', views.UserRegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.UserLoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.UserLogout, name='logout'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'), #{'next_page': '/successfully_logged_out/'}

    # Urls for categories
    url(r'^categories$', login_required(views.categories), name='categories'),
    url(r'^categories/all$', login_required(views.categories_all), name='categories_all'),
    url(r'^categories/add$', login_required(views.categories_add), name='categories_add'),
    url(r'^categories/delete$', login_required(views.categories_delete), name='categories_delete'),
    url(r'^categories/edit$', login_required(views.categories_edit), name='categories_edit'),

    # Urls for subcategories
    url(r'^subcategories$', login_required(views.subcategories), name='subcategories'),
    url(r'^subcategories/all$', login_required(views.subcategories_all), name='subcategories_all'),
    url(r'^subcategories/add$', login_required(views.subcategories_add), name='subcategories_add'),
    url(r'^subcategories/delete$', login_required(views.subcategories_delete), name='subcategories_delete'),
    url(r'^subcategories/edit$', login_required(views.subcategories_edit), name='subcategories_edit'),


    #Urls for products
    url(r'^products/$', login_required(views.IndexView.as_view()), name='products'),
    url(r'^products/add$', login_required(views.ProductCreate.as_view()), name='add_product'),

    url(r'^products/(?P<pk>[0-9]+)/$', login_required(views.ProductUpdate.as_view()), name='update_product'),

    url(r'^products/(?P<pk>[0-9]+)/delete/$', login_required(views.ProductDelete.as_view()), name='delete_product'),


]