from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product):

    allImages = cmod.ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'allImages': allImages,
    }

    return request.dmp.render('product.html', context)

#### This is where AJAX ends
@view_function
def tile(request, product:cmod.Product):
      
    context = {
        'product': product
    }

    return request.dmp.render('product.tile.html', context)