from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PagesForm
from .models import Book, Reader, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'bookcollector'

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
    readers_book_doesnt_have = Reader.objects.exclude(id__in = book.readers.all().values_list('id'))
    pages_form = PagesForm()
    return render(request, 'books/details.html', {'book': book, 'pages_form': pages_form, 'readers': readers_book_doesnt_have})

def add_pages(request, book_id):
    form = PagesForm(request.POST)
    if form.is_valid():
        new_pages = form.save(commit=False)
        new_pages.book_id = book_id
        new_pages.save()
    return redirect('details', book_id= book_id)

def assoc_reader(request, book_id, reader_id):
  Book.objects.get(id=book_id).readers.add(reader_id)
  return redirect('details', book_id=book_id)

def add_photo(request, book_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, book_id=book_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', book_id=book_id)

def unassoc_reader(request, book_id, reader_id):
  Book.objects.get(id=book_id).reader.remove(reader_id)
  return redirect('details', book_id=book_id)

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

class ReadersDetails(DetailView):
    model = Reader

class ReadersCreate(CreateView):
    model = Reader
    fields = '__all__'



