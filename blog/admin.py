from django.contrib import admin
from .models import Post

models = [Post]

for models in models:
    admin.site.register(models)
