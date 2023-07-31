from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article, Author


class Command(BaseCommand):
    help = 'Get articles by author ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('amount', type=int, help='Articles amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        amount = kwargs.get('amount')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            articles = Article.objects.filter(author=author)
            if amount is None:
                intro = f'All articles of {author}\n'
                text = '\n'.join(article.title for article in articles)
            else:
                intro = f'{amount} articles of {author}\n'
                i = 0
                text = ''
                for article in articles:
                    while i < amount
                    text.join(article.title).join('\n')
                    i += 1
            self.stdout.write(f'{intro}{text}')
