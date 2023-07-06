PLUGIN_NAME = "INTERCLOUD"
INSTALLED_APPS = [
    ...,
    "intercloud"
]

INSTALLED_PLUGINS = {
    "INTERCLOUD": {
        "version": "1.0.0",
        "product_model": "clients.models.Product",
        "data": {
            "link": lambda index, product: reverse("client_product_detail", 
                kwargs={"linker": product.user.business_name_lookup, "id": product.id}),
            "image": lambda index, product: product.image.path,
            "name": "name",
            "description": "description",
            "amount": None,
            "unit": None,
            "price": None,
            "coin": lambda index, product: product.user.configuration_set.first().coin,
            "add_msg": lambda *args: "Added",
            "rem_msg": lambda *args: "Removed",
            "link_add": lambda index, product: reverse("cart_multi_add", 
                kwargs={"cart_id": product.user.id, "id": product.id
            })
        }
    }
}
#ROOT_URLCONF = 'intercloud.urls'