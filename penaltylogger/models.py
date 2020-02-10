from django.db import models

#以下model。イベント、ラウンド、ジャッジ、選手、違反の内容、ペナルティの内容、備考。
class Event(models.Model):
    name = models.CharField(max_length=50)

class Round(models.Model):
     round_name = models.IntegerField()

class Judge(models.Model):
     judge_id = models.IntegerField()
     name = models.CharField(max_length=10)

class Player(models.Model):
     player_id = models.IntegerField()
     content = models.CharField(max_length=10)

class Violation(models.Model):
     content = models.CharField(max_length=30)

class Penalty(models.Model):
     content = models.CharField(max_length=10)

class Remarks(models.Model):
     text = models.TextField()

class Post(models.Model):
     event = models.ForeignKey(Event, on_delete=models.CASCADE)
     round = models.ForeignKey(Round, on_delete=models.CASCADE)
     judge_id = models.ForeignKey(Judge, on_delete=models.CASCADE)
     player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
     violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
     penalty = models.ForeignKey(Penalty, on_delete=models.CASCADE)
     remarks = models.ForeignKey(Remarks, on_delete=models.CASCADE)
     