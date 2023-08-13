from django.urls import path
from . import views

urlpatterns = [
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client_products/<int:client_id>/<str:period>/', views.client_products, name='client_products'),
    path('client_add/', views.client_add, name='client_add'),
    path('product_add/', views.product_add, name='product_add'),
    path('client_update/', views.client_update, name='client_update'),
    path('product_update/', views.product_update, name='product_update'),
]
