from django.urls import path
from . import views

urlpatterns = [
    path('headsortails/', views.headsortails, name='headsortails'),
    path('dice/', views.dice, name='dice'),
    path('randnumber/', views.randnumber, name='randnumber'),
]
