from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Order


class Command(BaseCommand):
    help = 'Update order by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('client', type=int, help='Client ID')
        parser.add_argument('products', type=list, help='Products list')
        parser.add_argument('total_price', type=float, help='Products total price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if kwargs.get('client'):
            order.client = kwargs.get('client')
        if kwargs.get('products'):
            order.products = kwargs.get('products')
        if kwargs.get('total_price'):
            order.total_price = kwargs.get('total_price')
        order.save()
        self.stdout.write(f'{order}')
