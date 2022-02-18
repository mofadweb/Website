from django.contrib import admin
from .models import Board,  Leader

models = [Board, Leader]

for models in models:
    admin.site.register(models)
