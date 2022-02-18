from django.shortcuts import render
from django.views import generic

from .models import Board


class BoardListView(generic.ListView):
    model = Board
    template_name = 'leadership/board_list.html'
    context_object_name = 'boards'


class BoardDetailView(generic.DetailView):
    model = Board
    template_name = 'leadership/board_detail.html'
    context_object_name = 'board'
