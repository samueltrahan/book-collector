from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.book_details, name='details'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name="books_update"),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name="books_delete"),
    path('books/<int:book_id>/add_pages/', views.add_pages, name='add_pages'),
    path('books/<int:book_id>/assoc_reader/<int:reader_id>/', views.assoc_reader, name='assoc_reader'),
    path('books/<int:book_id>/unassoc_reader/<int:reader_id>/', views.unassoc_reader, name='unassoc_reader'),
    path('books/<int:book_id/add_photo/', views.add_photo, name="add_photo"),
    path('readers/', views.ReadersList.as_view(), name="readers_index"),
    path('readers/<int:pk>/', views.ReadersDetails.as_view(), name="readers_detail"),
    path('readers/create/', views.ReadersCreate.as_view(), name="reader_create"),
    path('books/<int:book_id>/add_photo/', views.add_photo, name='add_photo'),
]