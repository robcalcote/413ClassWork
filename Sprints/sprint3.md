# # Sprint 3: Catalog

Sprint 3 is about the /catalog/ app, product models, recent views, and shopping cart.

`version 1.0`
|----------------------------|
| #X# Catalog App            |
|----------------------------|
#X# Create a "catalog" app and add to INSTALLED_APPS
#X# Download a number of product pictures to `/catalog/media/products/`

|----------------------------|
| #X# Category Model         |
|----------------------------|
#X# Create in /catalog/models.py -> class Category(models.Model)
#X# Required fields:
  #X# last_modified - models.DatetimeField, auto_now=True
  #X# name - models.TextField

|----------------------------|
| #X# Product Model          |
|----------------------------|
#X# Create in /catalog/models.py -> class Product(models.Model)
#X# Required fields:
  #X# category (1-M foreign key to Category model) - models.ForeignKey
  #X# last_modified - models.DatetimeField, auto_now=True
  #X# status - models.TextField, db_index=True, choices=Active or Inactive, default=, don't use boolean field
  #X# name - models.TextField
  #X# description - models.TextField
  #X# price - models.DecimalField, max_digits=(you decide), decimal_places=2
  #X# quantity (current in stock) - models.IntegerField
  #X# reorder_trigger (when we reorder) - models.IntegerField
  #X# reorder_quantity (how many we order) - models.IntegerField
#X# Required methods:
  #X# image_url(self) - return an absolute URL to the first image for this product, or if no ProductImage records, the "no image available" image. The return will be something like: `settings.STATIC_URL + "catalog/media/products/rustic-violin.jpg"`
  #X# images_url(self) - return a list of absolute URLs to the images for this product, or if no ProductImage records, a list of one item: the "no image available" image.

|----------------------------|
| #X# ProductImage Model     |
|----------------------------|
#X# Create in /catalog/models.py -> class ProductImage(models.Model)
#X# Required Fields:
  #X# filename - models.TextField(), example: "violin.jpg"
  #X# product (1-M foreign key to Product model) - models.ForeignKey
#X# Required Methods
  #X# image_url(self) - return an absolute URL to this image. The return will be something like: `settings.STATIC_URL + "catalog/media/products/rustic-violin.jpg"`. If no images available, return something like: `settings.STATIC_URL + "catalog/media/products/notfound.jpg"`

|----------------------------|
| #X# Fixtures               |
|----------------------------|
#X# Create a fixtures file in /catalog/fixtures/catalog.yaml or /catalog/fixtures/catalog.json
  #X# 3+ categories
  #X# 6+ active products per category
  #X# 1+ inactive products
  #X# 2+ product images per product
    #X# Except one product should have no images (it will display the "no image available" default image).

Management commands can be helpful here:

#X# Export database to fixtures file: `python3 manage.py dumpdata --format yaml catalog > catalog/fixtures/catalog.yaml`
#X# Import fixtures file into database: "python3 manage.py loaddata catalog/fixtures/catalog.yaml"
 
|----------------------------|
| #X# `/catalog/templates    |
|     /app_base.htm`         |
|----------------------------|
#X# Extends /homepage/templates/base.htm
#X# Override the left column block
  #X# Show all category names in a `<ul>` list
  #X# In /catalog/styles/app_base.scss, style the list so it has no bullets or margin. It will look the same on the screen as if it were a series of `<div>` elements.
  #X# Each name links to `/catalog/index/<category id>/`
  #X# For all products: `/catalog/index/`
#X# All pages in the catalog app extend from this template

|----------------------------|
| # # List of Products (Category) Page: `/catalog/index/<category id>/<page number>/`   
|----------------------------|
#X# Shows product tiles for the given category
  #X# Only products with "active" status are shown
  #X# Show up to 8 products per page
#X# View function is: `def process_request(request, category:cmod.Category=None, page:int=1)`
  #X# DMP docs: https://django-mako-plus.readthedocs.io/converters_types.html
  #X# If `category` is None, show all products
  #X# If `category` is given, show that category's products
#X# Product tiles should be loaded with ajax calls to `/catalog/product.tile/<product id>/`
  #X# Create a `<div class="product-container" data-product-id="${ product.id }"></div>` container to load into
  #X# Use jQuery's `$.ajax` or `$.load` commands in `/catalog/scripts/catalog.js`
  #X# DMP docs: https://django-mako-plus.readthedocs.io/static_overview.html, especially Step 2, ES5 JS, run when page is ready (jQuery).
#X# Paginate up to 8 items per page
  #X# Pagination is on SERVER SIDE with a query, not on client side with JS
  #X# Previous Page and Next Page links at bottom of product tiles
  #X# Example of all products, page 3: `<a class="btn btn-default" href="/catalog/index/0/3/">Next Page</a>`
  #X# Example of instruments category (id=7), page 2: `<a class="btn btn-default" href="/catalog/index/7/2/">Next Page</a>`
#X# Hints:
  #X# If `products` is a query, then `math.ceil(products.count() / ITEMS_PER_PAGE)` gives the number of pages.
  #X# If `products` is a query of all products, then `products = products.filter(...)` filters the query further (i.e. to a category).
  #X# If `products` is a query of all products, then `products = products[8:16]` filters the query to records 8-15 inclusive.
  #X# `<%! from catalog import models as cmod %>` makes `cmod` available in `app_base.htm`.

|----------------------------|
| #X# Product Detail Page:   | 
| `/catalog/product/<product id>/`
|----------------------------|
#X# View file is in `/catalog/views/product.py`
  #X# View function is: `def process_request(request, product:cmod.Product)`
#X# Template file is `/catalog/templates/product.html`
  #X# Extends `/catalog/templates/app_base.htm"
#X# Displays similar to an Amazon.com page
  #X# All images for the product
  #X# All fields: name, description, price, etc.
#X# Functionality NOT in in this sprint:
  #X# No purchase button yet
  #X# No quantity available display yet

|----------------------------|
| #X# Product Tile Snippet:  |
| `/catalog/product.tile/<product id>/`
|----------------------------|
#X# DMP docs: https://django-mako-plus.readthedocs.io/tutorial_ajax.html
#X# View file is in `/catalog/views/product.py`
  #X# View function is: `def tile(request, product:cmod.Product)`
#X# Template file is `/catalog/templates/product.tile.html`
  #X# Extends `/homepage/templates/base_ajax.htm"
#X# Style the classes with CSS in `/catalog/styles/product.tile.scss`
  #X# `product-tile`
    #X# display set to `inline-block`
    #X# max-width set to something like 300px
    #X# border set to something
    #X# border-radius set to 5px or similar
  #X# `product-image`
    #X# sets a max-width on the image
    #X# centers the image horizontally
  #X# `product-name` and `product-price`
    #X# centers the text horizontally
    #X# displays under the image
All done below
Example HTML for the tile:
```html
<a href="/catalog/product/1234/">
    <div class="product-tile">
        <div class="product-image"><img src="/static/catalog/media/products/violin.jpg"/></div>
        <div class="product-name">Violin</div>
        <div class="product-price">$156.00</div>
    </div>
</a>
```
