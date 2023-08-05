from django.shortcuts import render, get_object_or_404

from project_one.thirdapp.models import Author, Article, Comment


def author_articles(request, author_id):
    author = get_object_or_404(Author, pk = author_id)
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
    article = get_object_or_404(Article, pk=article_id)
    author = get_object_or_404(Author, pk=article.author.pk)
    comments = Comment.objects.filter(article=article).order_by('updated_at')
    context = {'article': article,
               'author': author,
               'comments': comments}
    article.views_number += 1
    article.save()
    return render(request, 'thirdapp/article_info.html', context)
