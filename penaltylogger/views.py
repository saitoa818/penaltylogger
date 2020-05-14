from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from .forms import LogForm
from .forms import LoginForm
from .models import Log, Event, Judge, Penalty, Player
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'registration/login.html'

class LogList(LoginRequiredMixin,ListView):
    model = Log
    fields = ['all']

    def get_queryset(self):
        current_user = self.request.user
        if current_user.log_view: 
            return Log.objects.all()
        else:
            return Log.objects.filter(judge_id=None)

@login_required
def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'penaltylogger/log_detail.html', {'log': log})

def log_new(request):
    if request.method == "GET": #入力を行う
        form = LogForm(request.GET)
        return render(request, "penaltylogger/log_new.html", {'form': form})

    if request.method == "POST": #入力されたものを確認する
        form = LogForm(request.POST)
        if form.is_valid():
            return render(request, "penaltylogger/log_confirm.html", {'form': form })
    else:
        form = LogForm()
    return render(request, 'penaltylogger/log_new.html', {'form': form})   

@login_required
def log_save(request): 
    if request.method == "POST":
        form = LogForm(request.POST)
        log = form.save(commit=False)
        event = Event.objects.filter(name='テストイベント1').first()
        #上のname=の部分はイベントごとに修正が必要。
        judge = request.user
        player = Player.objects.filter(player_no=form.data['player_no']).first()
        log.event = event
        log.judge = judge
        log.player = player
        log.save()
    else:
        form = LogForm()
    return render(request, 'penaltylogger/log_save.html', {})