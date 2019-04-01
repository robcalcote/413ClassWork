from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from decimal import Decimal
from account import models as amod
import math

@view_function
def process_request(request, sale:cmod.Sale):

    completed_sale_items = cmod.SaleItem.objects.filter(sale=sale)

    context = {
        'completed': completed_sale_items,
        'sale': sale,
    }

    return request.dmp.render('receipt.html', context)

