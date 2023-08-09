from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client {self.name} {self.email} {self.phone_number}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=0)
    added_at = models.DateField(auto_now_add=True)
    photo = models.ImageField()

    def __str__(self):
        return f'Product {self.title} {self.price} руб.'


class Order (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.client}\n{self.products}\n{self.total_price}'
