from django.db import models
import datetime

# Create your models here.

# Custom Models - not found in Django Documentation

# Category has a 1..* relationship with Products
##  Category can have many Products
class Category(models.Model):
    name = models.TextField("Category Name", null=False)
    ## auto_now_add - updates when created
    ## auto_now - updates every time save() is called
    created = models.DatetimeField("Created Date", auto_now_add=True)
    last_modified = models.DatetimeField("Modified Date", auto_now=True, null=False)

##  Product can have 1 and only 1 Category
class Product(models.Model):
    category = models.ForeignKey(Category, "Product Category", on_delete=models.CASCADE)