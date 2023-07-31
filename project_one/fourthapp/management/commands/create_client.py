from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Client


class Command(BaseCommand):
    help = 'Create client.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('phone', type=str, help='Phone')
        parser.add_argument('address', type=str, help='Address')

    def handle(self, *args, **kwargs):
        client = Client(name=kwargs['name'],
                        email=kwargs['email'],
                        phone_number=kwargs['phone'],
                        address=kwargs['address'])
        client.save()
        self.stdout.write(f'{client}')
