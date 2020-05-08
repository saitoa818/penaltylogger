from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class Manager(BaseUserManager):
    judge_id = models.IntegerField(null=True, unique=True)
    def create_user(self, judge_id, password=None,):
        if not judge_id:
            raise ValueError

        user = self.model(password=password, judge_id=judge_id)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, judge_id, password=None,):
        user = self.create_user(
            password=password,
            judge_id=judge_id,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Judge(AbstractBaseUser, PermissionsMixin):
    judge_id = models.IntegerField(
        verbose_name='Judge_ID',
        blank=True,
        null=True,
        default=0,
        unique=True,
    )
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    log_view =  models.BooleanField(default=True)

    objects = Manager()

    USERNAME_FIELD = 'judge_id'
    def __str__(self):
        return str(self.judge_id)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
######


class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    max_round = models.IntegerField(null=True, blank=True)


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

class Level(models.TextChoices):
     低 = '低', '低'
     中 = '中', '中'
     高 = '高', '高'
     イカサマ = 'イカサマ', 'イカサマ'
LEVEL_CHOICES = Level.choices

class Log(models.Model):
     event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=True, null=True)
     round = models.IntegerField(blank=True, null=True)
     judge = models.ForeignKey(Judge, on_delete=models.DO_NOTHING, blank=True, null=True)
     player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True)
     violation = models.ForeignKey(Violation, on_delete=models.DO_NOTHING, blank=True, null=True)
     penalty = models.ForeignKey(Penalty, on_delete=models.DO_NOTHING, blank=True, null=True)
     text = models.TextField(blank=True, null=True)
     level = models.TextField(choices=LEVEL_CHOICES)