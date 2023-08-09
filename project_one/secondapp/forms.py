from django import forms


class GameForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('coin', 'Монетка'), ('dice', 'Кубик'), ('number', 'Число')])
    attempt_amount = forms.IntegerField(min_value=1, max_value=64)
