from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ArticleForm, AuthorForm, CommentForm
from .models import Author, Article, Comment


def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(firstname=form.cleaned_data['firstname'],
                            lastname=form.cleaned_data['lastname'],
                            email=form.cleaned_data['email'],
                            biography=form.cleaned_data['biography'],
                            birthday=form.cleaned_data['birthday'])
            author.save()
            return HttpResponse(f'Автор {author.full_name()} добавлен успешно.')
    else:
        form = AuthorForm()
        return render(request, 'thirdapp/author_add.html', {'form': form})


def article_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article(title=form.cleaned_data['title'],
                              content=form.cleaned_data['content'],
                              author=get_object_or_404(Author, pk=int(form.cleaned_data['author'])),
                              category=form.cleaned_data['category'],
                              released=form.cleaned_data['released'])
            article.save()
            return HttpResponse('Статья добавлена успешно.')
    else:
        form = ArticleForm()
        return render(request, 'thirdapp/article_add.html', {'form': form})


def author_articles(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author).order_by('id')
    context = {'author': author,
               'articles': articles}
    return render(request, 'thirdapp/author_articles.html', context)


def article_full(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    article.views_number += 1
    article.save()
    return render(request, 'thirdapp/article_full.html', context)


def article_info(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=get_object_or_404(Author, pk=form.cleaned_data['author']),
                              article=get_object_or_404(Article, pk=article_id),
                              comment=form.cleaned_data['comment'])
            comment.save()
            return HttpResponse('Комментарий добавлен успешно.')
    else:
        form = CommentForm()
        article = get_object_or_404(Article, pk=article_id)
        author = get_object_or_404(Author, pk=article.author.pk)
        comments = Comment.objects.filter(article=article).order_by('updated_at')
        context = {'article': article,
                   'author': author,
                   'comments': comments,
                   'form': form}
        article.views_number += 1
        article.save()
        return render(request, 'thirdapp/article_info.html', context)
