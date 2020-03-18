from django.db import models
from django.contrib.auth.models import User

#以下model。イベント、ラウンド、ジャッジ、選手、違反の内容、ペナルティの内容、備考。
# class User
# メール
# password
# djangoのユーザーで調べる

class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    max_round = models.IntegerField(null=True, blank=True)

class Judge(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     judge_id = models.IntegerField(null=True, blank=True)
     name = models.CharField(max_length=10)

class Player(models.Model):
     player_no = models.IntegerField()
     player_name = models.CharField(max_length=10)

class Violation(models.Model):
     content = models.CharField(max_length=30)
     def __str__(self):
        return self.content

class Penalty(models.Model):
     content = models.CharField(max_length=10)
     def __str__(self):
        return self.content

class Log(models.Model):
     event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=True, null=True)
     round = models.IntegerField(blank=True, null=True)
     judge = models.ForeignKey(Judge, on_delete=models.DO_NOTHING, blank=True, null=True)
     player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True)
     violation = models.ForeignKey(Violation, on_delete=models.DO_NOTHING, blank=True, null=True)
     penalty = models.ForeignKey(Penalty, on_delete=models.DO_NOTHING, blank=True, null=True)
     text = models.TextField(blank=True, null=True)
     