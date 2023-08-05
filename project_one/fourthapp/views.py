import datetime

from project_one.fourthapp.models import Client, Order
from django.shortcuts import render, get_object_or_404


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).order_by('id')
    context = {'client': client,
               'orders': orders}
    return render(request, 'fourthapp/client_orders.html', context)


def client_products(request, client_id, period):
    if period == 'week':
        duration = 7
    elif period == 'month':
        duration = 30
    elif period == 'year':
        duration = 365
    else:
        duration = 14
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).filter(ordered_at__gte=datetime.date.today()
                                                        - datetime.timedelta(days=duration))
    products_set = set()
    for order in orders:
        for product in order.products:
            products_set.add(product)
    context = {'client': client,
               'duration': duration,
               'products_set': products_set}
    return render(request, 'fourthapp/client_products.html', context)

