from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog import models as cmod

# Create your models here.

# This model inherits from the Django AbstractUser model
# This can be found at django.contrib.auth.models
class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    birth_date = models.DateTimeField("User Birth Date", null=True)
    favorite_color = models.TextField("User Favorite Color", null=True)

    def get_shopping_cart(self):
        
        if cmod.Sale.objects.filter(user=self, purchased=None).count() == 0:
            cart = cmod.Sale(user=self, purchased=None)
            cart.save()
        else:
            cart = cmod.Sale.objects.get(user=self, purchased=None)
        return cart