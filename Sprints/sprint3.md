# Sprint 3: Catalog

Sprint 3 is about the /catalog/ app, product models, recent views, and shopping cart.

`version 1.0`

## Catalog App

* Create a "catalog" app and add to INSTALLED_APPS
* Download a number of product pictures to `/catalog/media/products/`

## Category Model

* Create in /catalog/models.py -> class Category(models.Model)
* Required fields:
  * last_modified - models.DatetimeField, auto_now=True
  * name - models.TextField

## Product Model

* Create in /catalog/models.py -> class Product(models.Model)
* Required fields:
  * category (1-M foreign key to Category model) - models.ForeignKey
  * last_modified - models.DatetimeField, auto_now=True
  * status - models.TextField, db_index=True, choices=Active or Inactive, default=, don't use boolean field
  * name - models.TextField
  * description - models.TextField
  * price - models.DecimalField, max_digits=(you decide), decimal_places=2
  * quantity (current in stock) - models.IntegerField
  * reorder_trigger (when we reorder) - models.IntegerField
  * reorder_quantity (how many we order) - models.IntegerField
* Required methods:
  * image_url(self) - return an absolute URL to the first image for this product, or if no ProductImage records, the "no image available" image. The return will be something like: `settings.STATIC_URL + "catalog/media/products/rustic-violin.jpg"`
  * images_url(self) - return a list of absolute URLs to the images for this product, or if no ProductImage records, a list of one item: the "no image available" image.

## ProductImage Model

* Create in /catalog/models.py -> class ProductImage(models.Model)
* Required Fields:
  * filename - models.TextField(), example: "violin.jpg"
  * product (1-M foreign key to Product model) - models.ForeignKey
* Required Methods
  * image_url(self) - return an absolute URL to this image. The return will be something like: `settings.STATIC_URL + "catalog/media/products/rustic-violin.jpg"`. If no images available, return something like: `settings.STATIC_URL + "catalog/media/products/notfound.jpg"`

## Fixtures

* Create a fixtures file in /catalog/fixtures/catalog.yaml or /catalog/fixtures/catalog.json
  * 3+ categories
  * 6+ active products per category
  * 1+ inactive products
  * 2+ product images per product
    * Except one product should have no images (it will display the "no image available" default image).

Management commands can be helpful here:

* Export database to fixtures file: `python3 manage.py dumpdata --format yaml catalog > catalog/fixtures/catalog.yaml`
* Import fixtures file into database: "python3 manage.py loaddata catalog/fixtures/catalog.yaml"

## `/catalog/templates/app_base.htm`

* Extends /homepage/templates/base.htm
* Override the left column block
  * Show all category names in a `<ul>` list
  * In /catalog/styles/app_base.scss, style the list so it has no bullets or margin. It will look the same on the screen as if it were a series of `<div>` elements.
  * Each name links to `/catalog/index/<category id>/`
  * For all products: `/catalog/index/`
* All pages in the catalog app extend from this template

## List of Products (Category) Page: `/catalog/index/<category id>/<page number>/`

* Shows product tiles for the given category
  * Only products with "active" status are shown
  * Show up to 8 products per page
* View function is: `def process_request(request, category:cmod.Category=None, page:int=1)`
  * DMP docs: https://django-mako-plus.readthedocs.io/converters_types.html
  * If `category` is None, show all products
  * If `category` is given, show that category's products
* Product tiles should be loaded with ajax calls to `/catalog/product.tile/<product id>/`
  * Create a `<div class="product-container" data-product-id="${ product.id }"></div>` container to load into
  * Use jQuery's `$.ajax` or `$.load` commands in `/catalog/scripts/catalog.js`
  * DMP docs: https://django-mako-plus.readthedocs.io/static_overview.html, especially Step 2, ES5 JS, run when page is ready (jQuery).
* Paginate up to 8 items per page
  * Pagination is on SERVER SIDE with a query, not on client side with JS
  * Previous Page and Next Page links at bottom of product tiles
  * Example of all products, page 3: `<a class="btn btn-default" href="/catalog/index/0/3/">Next Page</a>`
  * Example of instruments category (id=7), page 2: `<a class="btn btn-default" href="/catalog/index/7/2/">Next Page</a>`
* Hints:
  * If `products` is a query, then `math.ceil(products.count() / ITEMS_PER_PAGE)` gives the number of pages.
  * If `products` is a query of all products, then `products = products.filter(...)` filters the query further (i.e. to a category).
  * If `products` is a query of all products, then `products = products[8:16]` filters the query to records 8-15 inclusive.
  * `<%! from catalog import models as cmod %>` makes `cmod` available in `app_base.htm`.

## Product Detail Page: `/catalog/product/<product id>/`

* View file is in `/catalog/views/product.py`
  * View function is: `def process_request(request, product:cmod.Product)`
* Template file is `/catalog/templates/product.html`
  * Extends `/catalog/templates/base.htm"
* Displays similar to an Amazon.com page
  * All images for the product
  * All fields: name, description, price, etc.
* Functionality NOT in in this sprint:
  * No purchase button yet
  * No quantity available display yet

## Product Tile Snippet: `/catalog/product.tile/<product id>/`

* DMP docs: https://django-mako-plus.readthedocs.io/tutorial_ajax.html
* View file is in `/catalog/views/product.py`
  * View function is: `def tile(request, product:cmod.Product)`
* Template file is `/catalog/templates/product.tile.html`
  * Extends `/homepage/templates/base_ajax.htm"
* Style the classes with CSS in `/catalog/styles/product.tile.scss`
  * `product-tile`
    * display set to `inline-block`
    * max-width set to something like 300px
    * border set to something
    * border-radius set to 5px or similar
  * `product-image`
    * sets a max-width on the image
    * centers the image horizontally
  * `product-name` and `product-price`
    * centers the text horizontally
    * displays under the image

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