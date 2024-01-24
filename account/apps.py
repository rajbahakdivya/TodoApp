from django.apps import AppConfig


class OtpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'
    
    def ready(self):
      import account.signals