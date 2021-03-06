# Sprint 4: Checkout

Sprint 4 is the purchase process.

`version 1.0`

#X# Sale and SaleItem Models
#X# Create the Sale and SaleItem classes in `/catalog/models.py`:

    #X# from decimal import Decimal
    #X# TAX_RATE = Decimal("0.05")

    #X# class Sale(models.Model):
        user = models.ForeignKey("account.User", on_delete=models.PROTECT)
        created = models.DateTimeField(auto_now_add=True)
        purchased = models.DateTimeField(null=True, default=None)
        subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

        #X# def recalculate(self):
            '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
            # complete this method!

        #X# def finalize(self, stripeToken):
            '''Finalizes the sale'''
            # complete this method!
            # Ensure this sale isn't already finalized (purchased should be None)
            # Check product quantities one more time
            # Call recalculate one more time
            # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)
                # be sure to pip install stripe and import stripe into this file
            # Set purchased=now and charge_id=the id from Stripe
            # Save

    #X# class SaleItem(models.Model):
        STATUS_CHOICES = [
            ( 'A', 'Active' ),
            ( 'D', 'Deleted' ),
        ]
        status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
        sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
        product = models.ForeignKey("Product", on_delete=models.PROTECT)
        quantity = models.IntegerField(default=0)
        price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        class Meta:
            ordering = [ 'product__name' ]

#X# In the `Sale` class above, note the `recalculate` method, which should recalculate the Sale fields based on its current SaleItem objects. Be sure to skip any deleted SaleItems.


#X# Write the methods for the class Models above (Sale Methods)


#X# `user.get_shopping_cart()`
#X# Add the following method to your User model. This is an example of a convenience function:
    class User(AbstractUser):
        ...
        def get_shopping_cart(self):
            from catalog import models as cmod
            # retrieve (or create) a Sale with purchased=None for this user
            # return the Sale object
#X# Throughout your code, you can now use: `sale = request.user.get_shopping_cart()`


#X# "Purchase this Item" Form: `/catalog/product/<pid>/`
#X# Add a Django-style form:
   #X# A quantity text field.
   #X# A "Buy Now" button.
#X# Form validation/finish on the server:
  #X# Clean method should ensure the user is logged in (if not, redirect to login page). Unauthenticated users cannot have a shopping cart.
  #X# Clean method should also check quantity available and return "quantity not available" message if needed. Be sure to include any quantity already in the user's cart.
  #X# If form is valid, create or get the user's shopping cart Sale object (purchased=None), add a SaleItem record, and forward to shopping cart page: HttpResponseRedirect('/catalog/cart/').
  #X# If the product is already in the user's cart, adjust the quantity instead of adding a new `SaleItem`.
 

#X# Shopping Cart: `/catalog/cart/`
  #X# Show a table of products and quantities in the user's shopping cart Sale object (purchased=None). Be sure to skip any deleted SaleItems. The columns are as shown in the following example:
| Product Image   | Product Name          | Quantity | Price | Extended | Actions |
|-----------------|-----------------------|----------|-------|----------|---------|
| ` -OᵔO- `       | Piano Teacher Glasses | 2        | 30.00 |   60.00  | Remove  |
| ` o--|||---<| ` | Trumpet               | 1        | 70.00 |   70.00  | Remove  |
|                 | Tax                   |          |       |    6.50  |         |
|                 | Total                 |          |       |  136.50  |         |

#X# In the table, the `Remove` button is a link `<a href="/catalog/cart.remove/<pid>">`.  In this view function:
  #X# Set the status of the SaleItem to 'D' (deleted) and save.
  #X# Update the sale object totals and save.
  #X# Then redirect the browser back to the `/catalog/cart` page.
#X# Show a row for tax, which we'll calculate at a flat 5% rate.
#X# Below the table, a "Checkout Now" button goes to the checkout page.



#X# Checkout Page: `/catalog/checkout/`
  #X# Show a form containing address fields: address, city, state, zip, etc.
#X# Create an account at https://stripe.com.
  # # Place your Stripe standard, testing key and secret in settings as `settings.STRIPE_PUBLIC_KEY` and `settings.STRIPE_SECRET_KEY`.
  #X# You can set `stripe.api_key` in settings as well.
#X# Use the Stripe.com "Checkout" method to show the payment control.
  #X# Note that Stripe offers several methods of collecting payments. We're using one at https://stripe.com/docs/checkout.
  #X# Your Django form should include a hidden "stripeToken" field to put the returned stripe token into: `stripeToken = forms.CharField(widget=forms.HiddenInput())`
#X# You don't need to validate the address fields. You can assume they are entered correctly.
#X# In the form's clean() method, do something like this:

        #X# def clean(self):
            try:
                self.sale.finalize(self.cleaned_data['stripeToken'])
            except Exception as e:
                raise forms.ValidationError('Error processing payment: {}'.format(e))

#X# See the Sale object above for ideas on the `finalize()` method.
#X# Upon successful form submission and charge:
  #X# Update product quantities in the database.
  #X# Update the `purchased` and `charge_id` fields in the shopping cart, which turns it into a real Sale.
  #X# Forward the user to the "receipt" page.



#X# Receipt: `/catalog/receipt/<saleid>/`
  #X# This page can show the receipt for any sale object
  #X# Show a table of products purchased (similar to the cart page)
