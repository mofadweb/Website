from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventsView, name='events'),
]
