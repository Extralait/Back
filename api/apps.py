from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

class AccountsConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signal