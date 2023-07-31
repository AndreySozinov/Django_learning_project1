from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return f'Author: {self.firstname} {self.lastname} {self.email}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_number = models.IntegerField(default=0)
    released = models.BooleanField(default=False)

    def __str__(self):
        return f'Article: {self.title} Author: {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by author {self.author} to article {self.article}: {self.comment}'
    