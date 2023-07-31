from django.db import models


class CoinToss(models.Model):
    toss = models.CharField(max_length=10)
    toss_time = models.TimeField(auto_now=True)

    def __str__(self):
        return f'Toss result: {self.toss}, time: {self.toss_time}'

    @staticmethod
    def statistics(n: int = 1):
        all_tosses = CoinToss.objects.all()
        eagles = 0
        tails = 0
        for i in range(len(all_tosses) - 1, len(all_tosses) - 1 - n, -1):
            if all_tosses[i].toss == 'Орёл':
                eagles += 1
            elif all_tosses[i].toss == 'Решка':
                tails += 1
        return {'eagles': eagles, 'tails': tails}

