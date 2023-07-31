from random import randint, choice

from django.http import HttpResponse
import logging

from .models import CoinToss

logger = logging.getLogger(__name__)


def headsortails(request):
    coin = choice(['Орёл', 'Решка'])
    coin_toss = CoinToss(toss=coin)
    coin_toss.save()
    logger.info(f'getting {coin}')
    logger.info(f'В базу данных добавлена запись: {coin_toss}')
    return HttpResponse(f'На монете: {coin}\n\n{coin_toss.statistics(10)}')


def dice(request):
    a = randint(1, 6)
    logger.info(f'random side of dice: {a}')
    return HttpResponse(f'На кубике выпало: {a}')


def randnumber(request):
    a = randint(0, 100)
    logger.info(f'random number: {a}')
    return HttpResponse(f'Случайное число: {a}')
