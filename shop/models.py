from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.CharField(max_length=1000)