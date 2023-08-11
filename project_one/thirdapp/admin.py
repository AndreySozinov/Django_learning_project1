from django.contrib import admin
from .models import Author, Article, Comment


class AuthorAdmin(admin.ModelAdmin):
    """Список авторов."""
    list_display = ['firstname', 'lastname', 'email', 'birthday']

    """Отдельный автор."""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['lastname', 'firstname'],
            },
        ),
        (
            'Личные данные',
            {
                'description': 'Электронная почта, день рождения',
                'fields': ['email', 'birthday'],
            },
        ),
        (
            'Биография',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['biography'],
            }
        ),
    ]


class ArticleAdmin(admin.ModelAdmin):
    """Список статей."""
    list_display = ['title', 'pub_date', 'author', 'category', 'views_number']

    """Отдельная статья."""
    readonly_fields = ['views_number', 'released']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Выходные данные',
            {
                'description': 'Автор, дата публикации, категория',
                'fields': ['author', 'pub_date', 'category'],
            },
        ),
        (
            'Контент',
            {
                'classes': ['collapse'],
                'description': 'Статья',
                'fields': ['content'],
            }
        ),
        (
            'Дополнительно',
            {
                'description': 'Количество просмотров и опубликование статьи',
                'fields': ['views_number', 'released']
            }
        ),
    ]


class CommentAdmin(admin.ModelAdmin):
    """Список комментариев."""
    list_display = ['author', 'article', 'comment', 'created_at', 'updated_at']

    """Отдельный комментарий."""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author', 'article'],
            },
        ),
        (
            'Комментарий',
            {
                'description': 'Текст комментария',
                'fields': ['comment'],
            },
        ),
        (
            'Дата, время',
            {
                'description': 'Время написания и изменения комментария',
                'fields': ['created_at', 'updated_at'],
            }
        ),
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
