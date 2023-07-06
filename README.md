# Intercloud
## Package Description
Intercloud allows you to include your site inside cloudfood platform by opening an API controller which serves information from your project (only products)
## How to
```sh
pip3 install intercloud
```
Add intercloud configurations to your settings.py as follows 
```py settings.py
INSTALLED_APPS = [
    ...,
    "intercloud"
]
INSTALLED_PLUGINS = {
    "INTERCLOUD": { # Mandatory
        "version": "1.0.0", # For versions compatibility
        "product_model": "clients.models.Product", # Your product's model (MANDATORY)
        "data": {
            "link": None, # Link where the product will redirect when clicking on it in the cloudfood platform, by default if None search for product_model.link
            "image": None, # Image of the product, default if None to product_model.image
            "name": None, # The name of the product if none retreive its value from product
            "description": None, # Description of the product, if none do as previouses elements
            "amount": None, # Amount of products in stock if not defined no amount will be shown... (EXPERIMENTAL YET)
            "unit": None, # The unit or metrics unit of the product for example, if pizza you may want to set this as units if rice you may want to set this as kg..
            "price": None, # The price of the product mandatory
            "coin": None, # The coin used when selling this product
            "add_msg": None, # A message to be shown when adding this product to car
            "rem_msg":, # A message to be shown when removing this product from car
            "link_add": # The link of the cart controller (DO NOT USE, MAY BE REMOVED SOON)
        }
    }
}
```
```py urls.py
from intercloud.urls import urlpatterns as icf_url
urlpatterns = [
    ...,
    path("intercloud/", include(icf_url))
]
```

```py
MIDDLEWARE = [
    "intercloud.middleware.IntercloudMiddleware"
]
```
In your cloudfood admin site go to Security -> User -> Business and set the External Link field to your base URL for example
let say your domain is:
https://yourdomain.com 
and you set your url path to "intercloud/" over the base which means you can find the API at https://yourdomain.com/intercloud/
so you must in the admin site in the above path set the external url to https://yourdomain.com/intercloud/.
## Testing it does work
Set in your site differents products. Go to search tab, and type the name of a product in your external site...
## Security

* If your IP is locked you wont be able to show your products in the site...
* For security reasons all external products will be cached 7 days (But site still must request products from external sites) 

Some security improvements may be added soon to restrict which users do communicate with this API.
 