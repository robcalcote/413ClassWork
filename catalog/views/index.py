from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog.models import Category, Product, ProductImage

from datetime import datetime, timezone

# Define the number of Items per Page
ITEMS_PER_PAGE = 3

@view_function
def process_request(request):

    context = {
        'Category': Category,
        'Product': Product,
        'ProductImage': ProductImage
    }

    return request.dmp.render('index.html', context)