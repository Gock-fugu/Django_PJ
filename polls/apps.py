from django.apps import AppConfig
from django.contrib.auth import get_user_model

class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"

    def ready(self):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="sdilnij@gmail.com",
                password="239c2c0ffd88d0ebf290247267b4ecfd3"
            )
