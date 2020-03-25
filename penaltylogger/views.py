from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LogForm
from .models import Log
from .models import Judge
from django.contrib.auth.decorators import login_required
from . import forms

def login(request):
    return render(request, 'registration/login.html', {})

@login_required
def log_list(request):
    return render(request, 'penaltylogger/log_list.html', {})

@login_required
def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'penaltylogger/log_detail.html', {'log': log})

@login_required
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
        user = request.user
        user.save()
        judge = Judge(user=user)
        judge.save()

        
        form = LogForm(request.POST)
        log = form.save(commit=False)
        log.save()
    else:
        form = LogForm()
    return render(request, 'penaltylogger/log_save.html', {})