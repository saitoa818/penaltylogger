from django import forms

from .models import Player
from .models import Log


class LogForm(forms.ModelForm):
    player_no = forms.IntegerField()
    #labels = {'player_no': 'プレイヤーNo.',}
    class Meta:
        model = Log
        fields = ('round', 'player_no', 'violation', 'penalty', 'text')
        labels = {
            'round': 'ラウンド数',
            'player_no': 'プレイヤーNo.',
            'violation': '違反内容',
            'penalty': 'ペナルティの内容',
            'text': '備考欄',
        }
        

#class PlayerForm(forms.Form):
#player_no = forms.IntegerField()
    