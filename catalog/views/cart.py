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

    for sale in cart:
        cartItems = cmod.SaleItem.objects.filter(sale=sale, status='A')
        sale.recalculate()

    # Data passed to the .html page
    context = {
        'cartItems': cartItems,
        'sale': sale
    }

    return request.dmp.render('cart.html', context)


'''
# This function is to remove a particular item from the cart. It receives the request and
# <pid> from the template. the cart is called and saleItems are grabbed based on the filters:
#    product=<pid> from template.
#    sale=sale object from the cart.
# the SaleItem that matches both the cart# (Sale object) and productid (<pid>) will have status set to 'D'
# Then the function is redirected to the cart. which should only display 'A' items.
'''
@view_function
def remove(request, product:cmod.Product):
    cart = request.user.get_shopping_cart()
    for sale in cart:
        saleItem=cmod.SaleItem.objects.get(product=product, sale=sale, status='A')
        saleItem.status = 'D'
        saleItem.save()

    return HttpResponseRedirect('/catalog/cart')