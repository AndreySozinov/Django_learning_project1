from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Product, Order


class Command(BaseCommand):
    help = 'Get products by order ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            intro = f'All products in {order}\n'
            text = '\n'.join(product.title for product in order.products)
            self.stdout.write(f'{intro}{text}')
