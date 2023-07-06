from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ICFExampleProduct(models.Model):
    """
        This is an example product model, do not inheritate from it or work with it, will be useless
    """
    image = models.ImageField(upload_to='productos/', verbose_name=_('Image'), 
        help_text=_('Recommended resolution 400x300'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    price = models.FloatField(default=0, verbose_name=_('Price'), help_text=_('Opcional'))
    description = models.TextField(verbose_name=_("Product description"), null=True, blank=True)
    is_featured = models.BooleanField("Es especial?", default=False)
    in_stock = models.BooleanField("Quedan existencias en la tienda?", default=True)
    amount = models.FloatField("Cantidad en el almacen", default=0)
    unit = models.CharField("Unidad de medida", 
        help_text="Por ejemplo: Unidades, Kilogramos, Libras, Litros etc...", max_length=40, default="")
    views = models.PositiveIntegerField("Cantidad de veces que este producto fue visto", default=0)
    buys = models.PositiveIntegerField("Cantidad de veces que este producto fue comprado", default=0)
    category = models.CharField("Categoria del producto", max_length=50, default="")

    #class Meta:
    #    abstract = True

class ICFProducts:
    __len = 0
    #__products = list()
    def __init__(self, initial_products=[]):
        self.__products = list()
        is_qs = type(initial_products) is models.QuerySet
        is_iter = hasattr(initial_products, "__iter__")
        if is_qs or is_iter:
            self.__products += initial_products
            if is_qs:
                self.__len += initial_products.count()
            elif is_iter:
                self.__len += len(initial_products)
        else:
            raise ValueError("Only iterables who implements __iter__ methods and QuerySets are allowed")
            

    def __add__(self, other):
        is_qs = type(other) is models.QuerySet
        is_iter = (type(other) is not str) and hasattr(other, "__iter__")
        if is_qs or is_iter: 
            self.__products += other
            if is_qs:
                self.__len += other.count()
            elif is_iter:
                self.__len += len(other)
        else:
            self.__products.append(other)
            self.__len += 1
        return self

    def __getitem__(self, index):
        i = 0
        for item in self.__products:
            if i == index:
                return item
            i += 1

    def __iter__(self, *args, **kwargs):
        for product in self.__products:
            is_qs = type(product) is models.QuerySet
            if is_qs:
                yield self.__qs_iterator(product)
            else: 
                yield product

    def __qs_iterator(self, qs: models.QuerySet):
        for i in range(qs.count):
            yield qs[i]

    def __len__(self, *args, **kwargs):
        return self.__len
    
    def __str__(self):
        return str(self.__products)
    
    def count(self, ):
        return self.__len__()

class ICFRemoteProduct:
    """
        holder class for remote products, this is not a Model is just a wrapper for handle remote
        products...
    """
    def __init__(self, *args, **kwargs):
        for attr in kwargs.keys():
            if attr in self.__dict__.keys():
                setattr(self, attr, kwargs.get(attr))

    link = None
    image = None
    name = None
    description = None
    amount = None
    unit = None
    price = None
    coin = None
