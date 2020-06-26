from django.contrib import admin
from .models import Book, Pages, Reader, Photo
# Register your models here.
admin.site.register(Book)
admin.site.register(Pages)
admin.site.register(Reader)
admin.site.register(Photo)
