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
def process_request(request, product:cmod.Product):
    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        form.product = product
        if form.is_valid():
            if request.user.is_authenticated:
                cart = request.user.get_shopping_cart()
                for item in cart:
                    if item.items.count() == 0: # This code is only reachable if the cart is totally empty
                        # add a new object
                        FirstItem=cmod.SaleItem(sale=item, product=product, quantity=form.data['quantity'], price=product.price)
                        FirstItem.save()
                    else: # possible outcomes - increment existing, add new
                        incrementExisting=cmod.SaleItem.objects.filter(sale=item, product=product, status='A')
                        if incrementExisting.count() > 0: # increment existing
                            for item in incrementExisting:
                                item.quantity += int(form.data['quantity'])
                                if (product.quantity < item.quantity):
                                    raise forms.ValidationError('quantity not available')
                                item.save()
                        else: # add new item
                            addNewItem=cmod.SaleItem(sale=item, product=product, quantity=form.data['quantity'], price=product.price)
                            addNewItem.save()
                return HttpResponseRedirect('/catalog/cart/')
            else:
                return HttpResponseRedirect('/account/login/')
        #else: # Invalid form
    else: # GET
        form = BuyNowForm()

    allImages = cmod.ProductImage.objects.filter(product=product)

    # Data passed to the .html page
    context = {
        'product': product,
        'allImages': allImages,
        'form': form,
    }

    return request.dmp.render('product.html', context)

class BuyNowForm(forms.Form):
    quantity = forms.CharField(label='Quantity', widget=forms.NumberInput())

    def clean(self):
        # also check the cart quantity
        quantity_available = int(self.product.quantity)
        print(quantity_available)
        quantity_requested = int(self.data['quantity'])
        if quantity_available < quantity_requested:
            raise forms.ValidationError('quantity not available')                       
        return self.cleaned_data




#### This is where AJAX ends
@view_function
def tile(request, product:cmod.Product):
      
    context = {
        'product': product
    }

    return request.dmp.render('product.tile.html', context)