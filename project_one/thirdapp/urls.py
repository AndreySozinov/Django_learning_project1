from django.urls import path
from . import views

urlpatterns = [
    path('author_full/<int:author_id>/', views.author_articles, name='author_articles'),
    path('article/<int:article_id>/', views.article_full, name='article_full'),
    path('article_info/<int:article_id>/', views.article_info, name='article_info'),
]