from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = '<h1>Главная</h1><h2>Сайт Django учебный</h2>' \
           '<p>Текст на главной странице.</p>' \
           '<p>Еще текст на главной странице</p>'
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = '<h1>Обо мне</h1><h2>Созинов Андрей</h2>' \
           '<p>Разработчик веб-приложений на Python</p>' \
           '<p>Фреймворк Django</p>'
    logger.info('About page accessed')
    return HttpResponse(html)
