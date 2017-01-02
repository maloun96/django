from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Urls for categories
    url(r'^categories', views.categories, name='categories'),
    url(r'^get_categories', views.get_categories, name='get_categories'),
    url(r'^category/add', views.category_add, name='category_add'),
    url(r'^category/delete', views.category_delete, name='category_delete'),

    url(r'^subcategories$', views.subcategories, name='categories'),
]