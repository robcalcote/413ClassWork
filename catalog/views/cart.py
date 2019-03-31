from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from account import models as amod
import math

@view_function
def process_request(request):

    cart = request.user.get_shopping_cart()

    for item in cart:
        cartItems = cmod.SaleItem.objects.filter(sale=item)

    # Data passed to the .html page
    context = {
        'cartItems': cartItems,
    }

    return request.dmp.render('cart.html', context)

@view_function
def remove(request, saleItem:cmod.SaleItem):
    saleItem.status = 'D'
    saleItem.save()

    return HttpResponseRedirect('/catalog/cart')