from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Reader
from .forms import PagesForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    pages_form = PagesForm()
    return render(request, 'books/details.html', {'book': book, 'pages_form': pages_form})

def add_pages(request, book_id):
    form = PagesForm(request.POST)
    if form.is_valid():
        new_pages = form.save(commit=False)
        new_pages.book_id = book_id
        new_pages.save()
    return redirect('details', book_id= book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'description']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'


class ReadersList(ListView):
    model = Reader

class ReadersDetail(DetailView):
    model = Reader

class ReadersCreate(CreateView):
    model = Reader
    fields = '__all__'

class ReadersUpdate(UpdateView):
    model = Reader
    fields = ['favorite-book']

class ReadersDelete(DeleteView):
    model = Reader
    success_url = '/readers/'