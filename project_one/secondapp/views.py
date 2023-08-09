from random import randint, choice

from django.http import HttpResponse, HttpRequest
import logging

from django.shortcuts import render
from .forms import GameForm
from .models import CoinToss

logger = logging.getLogger(__name__)


def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            attempt_amount = form.cleaned_data['attempt_amount']
            logger.info(f'Get {game_type=}, {attempt_amount=}.')
            match game_type:
                case 'coin':
                    return headsortails(request, number=attempt_amount)
                case 'dice':
                    return dice(request, number=attempt_amount)
                case 'number':
                    return randnumber(request, number=attempt_amount)
    else:
        form = GameForm()
        return render(request, 'secondapp/game_form.html', {'form': form})


def headsortails(request, number):
    result_list = [choice(['Орёл', 'Решка']) for _ in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # coin_toss = CoinToss(toss=coin)
    # coin_toss.save()
    # logger.info(f'getting {coin}')
    # logger.info(f'В базу данных добавлена запись: {coin_toss}')
    # return HttpResponse(f'На монете: {coin}\n\n{coin_toss.statistics(10)}')
    return render(request, 'secondapp/headsortails.html', context)


def dice(request, number):
    result_list = [randint(1, 6) for _ in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # logger.info(f'random side of dice: {a}')
    # return HttpResponse(f'На кубике выпало: {a}')
    return render(request, 'secondapp/dice.html', context)


def randnumber(request, number):
    result_list = [randint(0, 100) for _ in range(0, number)]
    context = {'result_list': result_list,
               'number': number}
    # logger.info(f'random number: {a}')
    # return HttpResponse(f'Случайное число: {a}')
    return render(request, 'secondapp/randnumber.html', context)
