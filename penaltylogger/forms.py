from django import forms

from .models import Player, Log
from django.contrib.auth.forms import (
    AuthenticationForm
)

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('round', 'player_no', 'violation', 'penalty', 'level', 'text')

        labels = {
            'round': 'ラウンド数',
            'player_no': 'プレイヤーNo.',
            'violation': '違反内容',
            'penalty': 'ペナルティの内容',
            'level':'ペナルティ程度',
            'text': '備考欄',
        }
    player_no = forms.IntegerField(label='プレイヤーNo.')

    #level = level.choices
    AUTH_USER_MODEL = 'penaltylogger.player_no'
        

#class PlayerForm(forms.Form):
#player_no = forms.IntegerField()
