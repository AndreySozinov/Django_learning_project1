from random import randint, choice

from django.http import HttpResponse
import logging

from django.shortcuts import render

from .models import CoinToss

logger = logging.getLogger(__name__)


def headsortails(request, number):
    result_list = [choice(['Орёл', 'Решка']) for i in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # coin_toss = CoinToss(toss=coin)
    # coin_toss.save()
    # logger.info(f'getting {coin}')
    # logger.info(f'В базу данных добавлена запись: {coin_toss}')
    # return HttpResponse(f'На монете: {coin}\n\n{coin_toss.statistics(10)}')
    return render(request, 'secondapp/headsortails.html', context)


def dice(request, number):
    result_list = [randint(1, 6) for i in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # logger.info(f'random side of dice: {a}')
    # return HttpResponse(f'На кубике выпало: {a}')
    return render(request, 'secondapp/dice.html', context)


def randnumber(request, number):
    result_list = [randint(0, 100) for i in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # logger.info(f'random number: {a}')
    # return HttpResponse(f'Случайное число: {a}')
    return render(request, 'secondapp/randnumber.html', context)
