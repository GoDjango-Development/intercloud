from django.apps import AppConfig, registry
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string

class IntercloudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'intercloud'
    product_model = None
    
    def ready(self, *args, **kwargs):
        configuration = settings.INSTALLED_PLUGINS.get("INTERCLOUD", None)
        if configuration is None or configuration.get("product_model", None) is None:
            raise ImproperlyConfigured("This app seems to be in the installed apps but seems\
like is not correctly configured in INSTALLED_PLUGINS. (TIP: Set configuration as \
shown in this project settings.py example)")
        self.product_model = import_string(configuration.get("product_model"))

    def get_product_model(self, ):
        return self.product_model
    
    @staticmethod
    def get_current_app(cls, *args, **kwargs):
        return registry.apps.get_app_config(cls.name)