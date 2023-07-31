from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Comment


class Command(BaseCommand):
    help = 'Create comment.'

    def add_arguments(self, parser):
        parser.add_argument('author', type=int, help='Comment author ID')
        parser.add_argument('article', type=int, help='Article ID')
        parser.add_argument('comment', type=str, help='Comment content')

    def handle(self, *args, **kwargs):
        comment = Comment(author=kwargs['author'],
                          article=kwargs['article'],
                          comment=kwargs['comment'])
        comment.save()
        self.stdout.write(f'{comment}')
