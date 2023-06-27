from django.apps import AppConfig

class IpzConfig(AppConfig):
    name = 'ipz'

    def ready(self):
        import ipz.signals