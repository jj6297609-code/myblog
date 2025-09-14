from django import forms
from blog.models import Blog, BlogCategory

class PubBlogForm(forms.Form):
    title = forms.CharField(max_length=200, min_length=2)
    content = forms.CharField(min_length=2, widget=forms.Textarea)
    category = forms.IntegerField()

