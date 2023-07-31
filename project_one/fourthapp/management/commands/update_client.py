from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Client


class Command(BaseCommand):
    help = 'Update client by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone_number', type=str, help='Client phone')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if kwargs.get('name'):
            client.name = kwargs.get('name')
        if kwargs.get('email'):
            client.email = kwargs.get('email')
        if kwargs.get('phone_number'):
            client.phone_number = kwargs.get('phone_number')
        if kwargs.get('address'):
            client.address = kwargs.get('address')
        client.save()
        self.stdout.write(f'{client}')
