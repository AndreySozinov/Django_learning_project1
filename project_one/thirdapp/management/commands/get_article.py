from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article


class Command(BaseCommand):
    help = 'Get article by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
        article.views_number += 1
        article.save()
