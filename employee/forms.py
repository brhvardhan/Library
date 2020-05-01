from django import forms
from django.forms import ModelForm
from .models import Books

class AddBookForm(ModelForm):
    # test = forms.CharField(max_length=100)
    class Meta:
        model = Books
        fields = ['Name', 'Author',"Total_quantity"]

