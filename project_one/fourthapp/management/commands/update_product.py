import decimal

from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Product


class Command(BaseCommand):
    help = 'Update product by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('title', type=str, help='Product title')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=decimal, help='Product price')
        parser.add_argument('amount', type=int, help='Product amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if kwargs.get('title'):
            product.title = kwargs.get('title')
        if kwargs.get('description'):
            product.description = kwargs.get('description')
        if kwargs.get('price'):
            product.price = kwargs.get('price')
        if kwargs.get('amount'):
            product.amount = kwargs.get('amount')
        product.save()
        self.stdout.write(f'{product}')
