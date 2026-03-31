from django import forms
from file.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Name of file',
                'class': 'form-control',
            })}
