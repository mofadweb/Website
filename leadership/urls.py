from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='boards'),
    path('<slug:slug>', views.BoardDetailView.as_view(), name='board-detail')
]
