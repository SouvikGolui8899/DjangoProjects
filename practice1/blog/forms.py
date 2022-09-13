from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    content = forms.CharField(label='Content', widget=forms.TextInput(attrs={"placeholder": "Your Content"}))
    class Meta:
        model = Article
        fields = [
            'title',
            'content'
        ]
