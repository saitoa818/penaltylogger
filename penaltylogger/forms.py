from django import forms

from .models import Player
from .models import Log

class LogForm(forms.ModelForm):
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
    player_no = forms.IntegerField(label='プレイヤーNo.')
    AUTH_USER_MODEL = 'penaltylogger.player_no'
    
        

#class PlayerForm(forms.Form):
#player_no = forms.IntegerField()
    