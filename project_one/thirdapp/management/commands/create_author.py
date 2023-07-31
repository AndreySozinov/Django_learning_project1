from django.core.management.base import BaseCommand

from project_one.thirdapp.models import Author


class Command(BaseCommand):
    help = 'Create author.'

    def add_arguments(self, parser):
        parser.add_argument('firstname', type=str, help='Author firstname')
        parser.add_argument('lastname', type=str, help='Author lastname')
        parser.add_argument('email', type=str, help='Author email')
        parser.add_argument('biography', type=str, help='Author biography')
        parser.add_argument('birthday', type=str, help='Author birthday')

    def handle(self, *args, **kwargs):
        author = Author(firstname=kwargs['firstname'],
                        lastname=kwargs['lastname'],
                        email=kwargs['email'],
                        biography=kwargs['biography'],
                        birthday=kwargs['birthday'],
                        )
        author.save()
        self.stdout.write(f'{author}')
