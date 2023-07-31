from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Article, Comment


class Command(BaseCommand):
    help = 'Get comments by article ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('amount', type=int, help='Comments amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        amount = kwargs.get('amount')
        article = Article.objects.filter(pk=pk).first()
        if article is not None:
            comments = Comment.objects.filter(article=article)
            if amount is None:
                intro = f'All comments to {article.title}\n'
                text = '\n'.join(comment.comment for comment in comments)
            else:
                intro = f'{amount} comments to {article.title}\n'
                i = 0
                text = ''
                for comment in comments:
                    while i < amount:
                        text.join(comment.comment).join('\n')
                        i += 1
            self.stdout.write(f'{intro}{text}')
