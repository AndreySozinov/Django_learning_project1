from django.urls import path
from . import views

urlpatterns = [
    path('headsortails/<int:number>/', views.headsortails, name='headsortails'),
    path('dice/<int:number>/', views.dice, name='dice'),
    path('randnumber/<int:number>/', views.randnumber, name='randnumber'),
]
