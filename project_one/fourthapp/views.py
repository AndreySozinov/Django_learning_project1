import datetime

from django.http import HttpResponse

from .forms import ProductAddForm, ClientAddForm, ClientUpdateForm
from .models import Client, Order, Product
from django.shortcuts import render, get_object_or_404


def client_add(request):
    if request.method == 'POST':
        form = ClientAddForm(request.POST)
        if form.is_valid():
            client = Client(name=form.cleaned_data['name'],
                            email=form.cleaned_data['email'],
                            phone_number=form.cleaned_data['phone_number'],
                            address=form.cleaned_data['address'])
            client.save()
            return HttpResponse(f'Покупатель {client.name} добавлен успешно.')
    else:
        form = ClientAddForm
        return render(request, 'fourthapp/client_add.html', {'form': form})


def client_update(request):
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST)
        if form.is_valid():
            client = get_object_or_404(Client, pk=form.cleaned_data['pk'])
            if client is not None:
                client.name = form.cleaned_data['name']
                client.email = form.cleaned_data['email']
                client.phone_number = form.cleaned_data['phone_number']
                client.address = form.cleaned_data['address']
                client.save()
            return HttpResponse(f'Данные покупателя {client.name} успешно обновлены.')
    else:
        form = ClientUpdateForm
        return render(request, 'fourthapp/client_update.html', {'form': form})


def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(title=form.cleaned_data['title'],
                              description=form.cleaned_data['description'],
                              price=form.cleaned_data['price'],
                              amount=form.cleaned_data['amount'],
                              photo=form.cleaned_data['photo'])
            product.save()
            return HttpResponse(f'Продукт {product.title} добавлен успешно.')
    else:
        form = ProductAddForm()
        return render(request, 'fourthapp/product_add.html', {'form': form})


def product_update(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product = get_object_or_404(Product, pk=form.cleaned_data['pk'])
            if product is not None:
                product.title = form.cleaned_data['title']
                product.description = form.cleaned_data['description']
                product.price = form.cleaned_data['price']
                product.amount = form.cleaned_data['amount']
                product.photo = form.cleaned_data['photo']
                product.save()
            return HttpResponse(f'Продукт {product.title} успешно обновлён.')
    else:
        form = ProductAddForm()
        return render(request, 'fourthapp/product_update.html', {'form': form})


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
