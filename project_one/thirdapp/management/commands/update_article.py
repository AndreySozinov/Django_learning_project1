from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article


class Command(BaseCommand):
    help = 'Update article by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('title', type=str, help='Article title')
        parser.add_argument('content', type=str, help='Article content')
        parser.add_argument('pub_date', type=str, help='Article publication date')
        parser.add_argument('author', type=int, help='Article author ID')
        parser.add_argument('category', type=str, help='Article category')
        parser.add_argument('released', type=bool, help='Article released')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.filter(pk=pk).first()
        if kwargs.get('title'):
            article.title = kwargs.get('title')
        if kwargs.get('content'):
            article.content = kwargs.get('content')
        if kwargs.get('pub_date'):
            article.pub_date = kwargs.get('pub_date')
        if kwargs.get('author'):
            article.author = kwargs.get('author')
        if kwargs.get('category'):
            article.category = kwargs.get('category')
        if kwargs.get('released'):
            article.released = kwargs.get('released')
        article.save()
        self.stdout.write(f'{article}')

