from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Client, Order


class Command(BaseCommand):
    help = 'Get orders by client ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            orders = Order.objects.filter(client=client)
            intro = f'All orders by {client}\n'
            text = '\n'.join(order.products for order in orders)
            self.stdout.write(f'{intro}{text}')
