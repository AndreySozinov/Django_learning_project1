from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Comment, Author


class Command(BaseCommand):
    help = 'Get comments by author ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('amount', type=int, help='Comments amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        amount = kwargs.get('amount')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            comments = Comment.objects.filter(author=author)
            if amount is None:
                intro = f'All comments by {author}\n'
                text = '\n'.join(comment.comment for comment in comments)
            else:
                intro = f'{amount} comments by {author}\n'
                i = 0
                text = ''
                for comment in comments:
                    while i < amount:
                        text.join(comment.comment).join('\n')
                        i += 1
            self.stdout.write(f'{intro}{text}')
