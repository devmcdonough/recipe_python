from django.shortcuts import render
# To display lists
from django.views.generic import ListView, DetailView
# to access Book model
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/main.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'