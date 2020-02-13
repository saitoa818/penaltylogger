from django.db import models

#以下model。イベント、ラウンド、ジャッジ、選手、違反の内容、ペナルティの内容、備考。
class Event(models.Model):
    name = models.CharField(max_length=50)
    max_round = models.IntegerField()

class Judge(models.Model):
     judge_id = models.IntegerField()
     name = models.CharField(max_length=10)

class Player(models.Model):
     player_no = models.IntegerField()
     player_name = models.CharField(max_length=10)

class Violation(models.Model):
     content = models.CharField(max_length=30)

class Penalty(models.Model):
     content = models.CharField(max_length=10)

class Log(models.Model):
     event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
     round = models.IntegerField()
     judge = models.ForeignKey(Judge, on_delete=models.DO_NOTHING)
     player = models.IntegerField()
     violation = models.ForeignKey(Violation, on_delete=models.DO_NOTHING)
     penalty = models.ForeignKey(Penalty, on_delete=models.DO_NOTHING)
     text = models.TextField()
     