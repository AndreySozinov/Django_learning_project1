from random import randint, choice

from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def headsortails(request):
    coin = choice['Орёл', 'Решка']
    logger.info(f'getting {coin}')
    return HttpResponse(f'На монете: {choice}')


def dice(request):
    a = randint(1, 6)
    logger.info(f'random side of dice: {a}')
    return HttpResponse(f'На кубике выпало: {a}')


def randnumber(request):
    a = randint(0, 100)
    logger.info(f'random number: {a}')
    return HttpResponse(f'Случайное число: {a}')
