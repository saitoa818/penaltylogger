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
    player_no = Player.objects.filter(name=player_no) #ここで参照をxxx_idから変更する？
    class Meta:
        model = Log
        fields = (
            'round',
            'player_no',
            'violation',
            'penalty',
            'level',
            'text',
            )

        labels = {
            'round': 'ラウンド数',
            'player_no': 'プレイヤーNo.',
            'violation': '違反内容',
            'penalty': 'ペナルティの内容',
            'level':'ペナルティ程度',
            'text': '備考欄',
        }
    player_no = forms.IntegerField(label='プレイヤーNo.', required=False)
    
    AUTH_USER_MODEL = 'penaltylogger.player_no'
    def __str__(self):
        return self.player_no

#class PlayerForm(forms.Form):
#player_no = forms.IntegerField()
