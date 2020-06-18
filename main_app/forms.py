from django.forms import ModelForm
from .models import Pages

class PagesForm(ModelForm):
  class Meta:
    model = Pages
    fields = ['date', 'pagesRead']