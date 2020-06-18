from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'book_id': self.id})

class Pages(models.Model):
    date = models.DateField()
    pages = models.IntegerField()