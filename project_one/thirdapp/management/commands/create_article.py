from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article


class Command(BaseCommand):
    help = 'Create article.'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Article title')
        parser.add_argument('content', type=str, help='Article content')
        parser.add_argument('author', type=int, help='Article author ID')
        parser.add_argument('category', type=str, help='Article category')

    def handle(self, *args, **kwargs):
        article = Article(title=kwargs['title'],
                          content=kwargs['content'],
                          author=kwargs['author'],
                          category=kwargs['category'])
        article.save()
        self.stdout.write(f'{article}')
