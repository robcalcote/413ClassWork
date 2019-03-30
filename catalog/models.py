from django.db import models
import datetime
from django.conf import settings
from decimal import Decimal
import stripe

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
##  Product can be many SaleItem(s) for different Sales
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
        return self.image_urls()[0]

    def image_urls(self):
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

# Change this tax rate and the model methods will update as well
TAX_RATE = Decimal("0.05")

##  Sale can have many SaleItem(s)
##  Sale can have 1 and only 1 User attached to it
class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    # Total = subtotal + Tax
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    # This will be imported from Stripe
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
        # necessary to instantiate item_subtotal as a decimal so that the math is accurate
        item_subtotal = Decimal("0")
        # This line is the same as:
        # for si in SaleItem.objets.filter(sale=self, status='A')
        for si in self.items.filter(status='A'):
            item_subtotal = si.quantity * si.price
            self.subtotal += item_subtotal        
        self.tax = (self.subtotal * TAX_RATE)
        self.total = (self.tax + self.subtotal)

    def finalize(self, stripeToken):
        '''Finalizes the sale'''
        # complete this method!
        # Ensure this sale isn't already finalized (purchased should be None)
        if self.purchased == None:
            # Check product quantities one more time
            for si in self.items.filter(status='A'):
                product_quantity = si.product.quantity
                if si.quantity > product_quantity:
                    raise ValueError('Quantity available is less than quantity requested.')
            # Call recalculate one more time
            self.recalculate()
        # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)

        # Set purchased=now and charge_id=the id from Stripe
        self.purchased = datetime.now()
        #self.charge_id = # id from Stripe
        # Save
        self.save()


##  SaleItem can be on 1 and only 1 Sale
##  SaleItem can be for 1 and only 1 product
class SaleItem(models.Model):
    STATUS_CHOICES = [
        # First option is the default - can be changed and code will update default
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    # This is an inner class for SaleItem
    class Meta:
        ordering = [ 'product__name' ]