from django.db import models
import datetime

# Create your models here.

# Custom Models - not found in Django Documentation
# Documentation for customizing django classes can be found at:
# https://docs.djangoproject.com/en/2.1/topics/db/models/

#### MODEL EXPLANATION ###############################
#                                                    #
#   Category ----- Product ----- ProductImage        #
#   Explanations of relationships are listed above   #
#   each class                                       #
#                                                    #
######################################################


##  Category can have many Products
class Category(models.Model):
    ## verbose_name standard convention is lower cases, django will set first letter to capital
    ### verbose_name= is automatic in the first argument (except Foreign Keys, must be specified)
    name = models.TextField(verbose_name="category name")
    ## auto_now_add - updates when created
    ## auto_now - updates every time save() is called
    created = models.DateTimeField("created date", auto_now_add=True)
    last_modified = models.DateTimeField("modified date", auto_now=True)

##  Product can have 1 and only 1 Category
##  Product can have many ProductImages
class Product(models.Model):
    # deletion from DB will cascade from Category down through product
    category = models.ForeignKey(Category, verbose_name="product category", 
    on_delete=models.CASCADE)
    ACTIVE_STATUS = (
        # First option is the default - can be changed and code will update default
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.TextField("product active status", db_index=True, 
    choices=ACTIVE_STATUS, default=ACTIVE_STATUS[0][0])
    name = models.TextField("product name")
    # Allowed to be null - maybe product description isn't known upon insertion
    description = models.TextField("product description", null=True)
    # see this webpage for info on max_digits:
    ## https://stackoverflow.com/questions/47103113/issue-with-decimalfield-max-digits-of-django-models
    price = models.DecimalField("product price", max_digits=6, decimal_places=2, null=True)
    quantity = models.IntegerField("current stock quantity", null=True)
    #! Not quite sure how this one is supposed to work yet... !#
    reorder_trigger = models.IntegerField(null=True)
    reorder_quantity = models.IntegerField("stock replenishment quantity", null=True)
    created = models.DateTimeField("created date", auto_now_add=True)
    last_modified = models.DateTimeField("modified date", auto_now=True)
    ## db_index=True adds an index to optimize searching if you plan on querying by thise column
    ### the downside is that everytime you do an insert, indexes need to be updated
    ## choices= is where you set the choices that can be selected
    ## default= see below how the default 'choice' is setup

    #### REQUIRED PRODUCT METHODS ####
    def image_url(self):
        "Return an absolute URL to the first image for this product."
        # return first absolute URL in the list returned from the method below.
        return self.images_url()[0]

    def images_url(self):
        "Return a list of absolute URLs to the images for this product."
        urlsList = []
        # Query to find those images where the productimage is the same as the self object
        # This does the same as the for loop, but instead of saving it to an object, it just loops
        # imagesList = ProductImage.objects.filter(product=self)
        for pi in ProductImage.objects.filter(product=self):
            urlsList.append(pi.image_url())
        # Check length of URLS list and add noimage if 0
        if len(urlsList) == 0:
            urlsList.append(settings.STATIC_URL + 'catalog/media/products/notfound.jpg')
        return urlsList
        

##  ProductImage can have 1 and only 1 Product
class ProductImage(models.Model):
    # deletion of product from db will set foreign key for product on image to null
    product = models.ForeignKey(Product, verbose_name="image's product", 
    on_delete=models.SET_NULL, related_name='images', null=True)
    # Example: "violin.jpg"
    # see method below to see how this will be appended on the absolute URL
    filename = models.TextField("product image filename")

    #### REQUIRED PRODUCTIMAGE METHODS ####
    def image_url(self):
        "Return an absolute URL to this image."
        return settings.STATIC_URL + 'catalog/media/products/' + self.filename
