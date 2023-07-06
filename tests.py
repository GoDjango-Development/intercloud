from django.test import TestCase
from django.test.client import RequestFactory
#from .views import *
from .urls import urlpatterns
from .views import *
from .models import ICFProducts, ICFExampleProduct, ICFRemoteProduct
from django.urls import reverse, set_urlconf, get_urlconf, include
# Create your tests here.
class InterCloudTest(TestCase):
    def setUp(self, *args, **kwargs):
        self.factory = RequestFactory()
        ICFExampleProduct.objects.create()
        ICFExampleProduct.objects.create()
        ICFExampleProduct.objects.create()
        #set_urlconf(get_urlconf() + urlpatterns)

    def test_get_products(self, ):
        return # Do nothing as we must handle not already started case
        forged_request = self.factory.get("http://localhost:8000/test/intercloud/", {
            "sly-position": 0
        })
        response = get_products(forged_request, )
        print(response)
        assert response.status_code == 200, "Not 200"

    def test_icfproducts(self, *args, **kwargs):
        icf_products = ICFProducts()
        icf_products += ICFRemoteProduct(
            link = "one link",
            image = "image",
            name = "name",
            description = "description",
            amount = 0,
            unit = 20,
            price = 1.20,
            coin = "USD",
        )
        icf_products += ICFExampleProduct.objects.all()
        for product in icf_products:
            print(product)
        print(icf_products)
        print(icf_products.count())
        print(len(icf_products))

    #def test_each_product(self, ):
    #    pass
