from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article


class Command(BaseCommand):
    help = 'Get all articles.'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        self.stdout.write(f'{articles}')
