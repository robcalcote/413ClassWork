from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math

# Define the number of Items per Page
ITEMS_PER_PAGE = 8

@view_function
def process_request(request, category:cmod.Category=None, page:int=1): #

    products = cmod.Product.objects.filter(status="A")
    if category is not None:
        products = products.filter(category=category)
        numpages = math.ceil(products.filter(category=category).count() /ITEMS_PER_PAGE)
    else:
        numpages = math.ceil(cmod.Product.objects.filter(status="A").count() / ITEMS_PER_PAGE)

    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]

    context = {
        'category': category,
        'products': products,
        'page': page,
        'numpages': numpages,
    }

    print(numpages)

    return request.dmp.render('index.html', context)