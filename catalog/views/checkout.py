from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from account import models as amod
from decimal import Decimal
import math


@view_function
def process_request(request):
    cart = request.user.get_shopping_cart()
    cart.recalculate()
    sale_total = int(Decimal(cart.total) * Decimal("100.0"))
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.sale = request.user.get_shopping_cart()
        if form.is_valid():
            return HttpResponseRedirect('/catalog/receipt/{}/'.format(form.sale.id))
    else: # GET
        form = CheckoutForm()

    context = {
        'cart': cart,
        'form': form,
        'sale_total': sale_total,
    }

    return request.dmp.render('checkout.html', context)

class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address', widget=forms.TextInput())
    city = forms.CharField(label='Shipping City', widget=forms.TextInput())
    state = forms.CharField(label='Shipping State', widget=forms.TextInput())
    zipcode = forms.CharField(label='Shipping Zip', widget=forms.TextInput())
    stripeToken = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))