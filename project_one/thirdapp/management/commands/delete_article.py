from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article


class Command(BaseCommand):
    help = 'Delete article by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        article = Article.objects.filter(pk=pk).first()
        if article is not None:
            article.delete()
        self.stdout.write(f'{article}')
