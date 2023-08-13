from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    """Список покупателей."""
    list_display = ['name', 'email', 'phone_number']

    """Отдельный покупатель."""
    readonly_fields = ['registered_at']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактные данные',
            {
                'description': 'Электронная почта, телефон',
                'fields': ['email', 'phone_number'],
            },
        ),
        (
            'Адрес',
            {
                'classes': ['collapse'],
                'description': 'Адрес покупателя',
                'fields': ['address'],
            }
        ),
        (
            'Дата регистрации',
            {
                'description': 'Дата',
                'fields': ['registered_at'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'price', 'amount']

    """Отдельный продукт."""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание и внешний вид',
            {
                'classes': ['collapse'],
                'description': 'Описание товара и изображение',
                'fields': ['description', 'photo'],
            },
        ),
        (
            'Цена, количество',
            {
                'description': 'Актуальная цена и количество в наличии',
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Дата регистрации',
            {
                'description': 'Дата внесения в базу данных',
                'fields': ['added_at'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['client', 'total_price', 'ordered_at']

    """Отдельный заказ."""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Список товаров в заказе',
            {
                'description': 'Перечень товаров в заказе',
                'fields': ['products'],
            },
        ),
        (
            'Стоимость, дата заказа',
            {
                'description': 'Общая стоимость товаров в заказе и дата покупки',
                'fields': ['total_price', 'ordered_at'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
