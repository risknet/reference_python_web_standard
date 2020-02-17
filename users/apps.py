from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # triggering signal
    def ready(self):
        import users.signals 
