from django.shortcuts import render
# To display lists
from django.views.generic import ListView, DetailView
# to access Book model
from .models import Book
# To protect class based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/main.html'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'