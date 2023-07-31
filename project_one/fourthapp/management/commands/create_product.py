import decimal

from django.core.management.base import BaseCommand

from project_one.fourthapp.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Product title')
        parser.add_argument('description', type=str, help='Description')
        parser.add_argument('price', type=decimal, help='Price')
        parser.add_argument('amount', type=int, help='Amount')

    def handle(self, *args, **kwargs):
        product = Product(title=kwargs['title'],
                          description=kwargs['description'],
                          price=kwargs['price'],
                          amount=kwargs['amount'])
        product.save()
        self.stdout.write(f'{product}')
