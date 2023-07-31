import decimal

from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Order


class Command(BaseCommand):
    help = 'Create order.'

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client ID')
        parser.add_argument('products', type=list, help='Products list')
        parser.add_argument('total_price', type=decimal, help='Total price')

    def handle(self, *args, **kwargs):
        order = Order(client=kwargs['client'],
                      products=kwargs['products'],
                      total_price=kwargs['total_price'])
        order.save()
        self.stdout.write(f'{order}')
