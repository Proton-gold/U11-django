from django import forms

from Book.models import Book


class DFModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'price',
        ]
