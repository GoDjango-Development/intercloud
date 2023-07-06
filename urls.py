from django.urls import path
from .views import get_products, get_product
urlpatterns = [
    path("", get_products, name="intercloud_products"),
    path("<int:id>/", get_product, name="intercloud_product")
]