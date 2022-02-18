from django.contrib import admin
from .models import Event

models = [Event]

for models in models:
    admin.site.register(models)
