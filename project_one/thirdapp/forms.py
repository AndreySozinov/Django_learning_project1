import datetime

from django import forms

from .models import Author


class AuthorForm(forms.Form):
    firstname = forms.CharField(min_length=3, max_length=100)
    lastname = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(initial=datetime.date.today(),
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class ArticleForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    authors = Author.objects.all()
    # authors_id = [author.pk for author in authors]
    # authors_name = [author.full_name() for author in authors]
    author = forms.ChoiceField(choices=[(author.pk, author.full_name()) for author in authors])
    category = forms.CharField(min_length=3, max_length=100)
    released = forms.BooleanField()


class CommentForm(forms.Form):
    author = forms.IntegerField(min_value=1)
    comment = forms.CharField(widget=forms.Textarea)
