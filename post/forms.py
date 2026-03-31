from django import forms
from post.models import Post


class SDModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  ' author',
                  'body']
