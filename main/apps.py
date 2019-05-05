from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
    '''
    This is enough to make sure that signals are registered. Handlers will 
    now be called for every new product image uploaded to the site.
    '''     
        from . import signals
