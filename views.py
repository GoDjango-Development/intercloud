from .apps import IntercloudConfig
from django.db.models import Model
from django.shortcuts import render
#from django.conf import settings
from django.apps.registry import apps
from django.core.exceptions import ImproperlyConfigured
from django.http.request import HttpRequest
from django.http.response import JsonResponse, HttpResponseNotFound
from SOSCombos import settings
from django.core import serializers
import json

# Create your views here.

def _get_product(request: HttpRequest, *args, **kwargs):
    
    try:
        index = int(request.GET.get("sly-position", -1))
    except ValueError:
        return HttpResponseNotFound
    
    if index == -1:
        index = kwargs.get("id", -1)
    else:
        index = kwargs.get("id", 0)
        
    config = apps.get_app_config(IntercloudConfig.name)
    model: Model = config.get_product_model()
    products=model.objects.all()
    
    if index < 0: #muestramelos todos 
     
        data = serializers.serialize('json', products, indent=4)      
   
    else: #si especifica alguna muestramelo 
        print("Para mostrar uno solo")
    #Esto es par atrabajar con el json para procesarlo q es lo q se va a mostrar
        product = products[index]
        data = settings.INSTALLED_PLUGINS.get("INTERCLOUD", {}).get("data", None).copy()
    
        if data is None:
            raise ImproperlyConfigured("This app seems to be in the installed apps but seems\
    like is not correctly configured in INSTALLED_PLUGINS. (TIP: Set data configuration as \
    shown in this project settings.py example)")
      
        for key in data.keys():
            value = data[key]
            if callable(value):
                data[key] = value(index, product)
            elif type(value) is str:
                data[key] = getattr(product, value)
            elif value is None:
                data[key] = getattr(product, key)
            else:
                raise ImproperlyConfigured("%s value must be a callable or str"%key)
        if products.count() - 1 == index:
            data["%signal%"] = "%.%"
    return JsonResponse(data, safe=False)



def get_products(request: HttpRequest, *args, **kwargs):
    return _get_product(request, *args, **kwargs)

def get_product(request: HttpRequest, *args, **kwargs):
    return _get_product(request, *args, **kwargs)

def get_product_amount(request: HttpRequest, *args, **kwargs):
    return JsonResponse({
        "length": apps.get_app_config(IntercloudConfig.name).get_product_model().objects.count()
    })