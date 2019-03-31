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
    #cart = request.User.get_shopping_cart()
    #cart.save()

    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.sale = request.User.get_shopping_cart()
        if form.is_valid():
            return HttpResponseRedirect('/catalog/receipt/{}/'.format(form.sale.id))
    else: # GET
        form = CheckoutForm()

    context = {
        #'cart': cart,
        'form': form,
    }

    return request.dmp.render('checkout.html', context)

class CheckoutForm(forms.Form):
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label='Shipping State')
    zipcode = forms.CharField(label='Shipping Zip')
    stripeToken = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))