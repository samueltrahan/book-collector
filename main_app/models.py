from django.db import models
from django.urls import reverse

# Create your models here.

class Reader(models.Model):
    name = models.CharField(max_length=50)
    favorite_book = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('readers_detail', kwargs={'pk': self.id})


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    readers = models.ManyToManyField(Reader)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'book_id': self.id})

class Pages(models.Model):
    date = models.DateField('reading date')
    pagesRead = models.IntegerField()

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_pagesRead_display()} on {self.date}"

    class Meta:
        ordering = ['-date']