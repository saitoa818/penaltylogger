from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LogForm
from .models import Log
from .models import Event
from .models import Judge
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import ListView


def login(request):
    return render(request, 'registration/login.html', {})

#@login_required('polls.add_choice')
class LogList(ListView):
    model = Log
    fields = ['all']

@login_required
def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'penaltylogger/log_detail.html', {'log': log})

@login_required('polls.add_choice')
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
        judge = request.user
        event = Event.objects.filter(name='テストイベント1').first()
        #name=の部分はイベントごとに修正が必要。
        log.event = event
        log.judge = judge
        log.save()
    else:
        form = LogForm()
    return render(request, 'penaltylogger/log_save.html', {})