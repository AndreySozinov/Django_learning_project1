import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    context = {'name': 'Andrew'}
    logger.info('Index page accessed')
    return render(request, 'firstapp/index.html', context)


def about(request):
    context = {'firstname': 'Андрей',
               'lastname': 'Созинов'}
    logger.info('About page accessed')
    return render(request, 'firstapp/about.html', context)
