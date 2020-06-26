from django.db import models
from django.urls import reverse



class Reader(models.Model):
    name = models.CharField(max_length=50)

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for book_id: {self.book_id} @{self.url}"