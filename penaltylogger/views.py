from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import LogForm
from .models import Log
from .models import Player
from django.contrib.auth.models import User
from . import forms

def login(request):
    return render(request, 'penaltylogger/login.html', {})

def log_list(request):
    return render(request, 'penaltylogger/log_list.html', {})

def log_detail(request, pk):
    log = get_object_or_404(Log, pk=pk)
    return render(request, 'penaltylogger/log_detail.html', {'log': log})

#def log_new(request):
    # if request.method == "POST":
    #     form = LogForm(request.POST)
    #     if form.is_valid():
    #         log = form.save(commit=False)
    #         log.author = request.user
    #         log.published_date = timezone.now()
    #         log.save()
    #         return redirect('log_detail', pk=log.pk)
    # else:
    #     form = LogForm()
    # return render(request, 'penaltylogger/log_edit.html', {'form': form})

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

def log_save(request): 
    if request.method == "POST":
        form = LogForm(request.POST)
        log = form.save(commit=False)
        log.save()
    else:
        form = LogForm()
    return render(request, 'penaltylogger/log_save.html', {})
    

# def log_edit(request, pk):
 #     log = get_object_or_404(Log, pk=pk)
 #     if request.method == "POST":
 #         form = LogForm(request.POST, instance=log)
 #         if form.is_valid():
 #             log = form.save(commit=False)
 #             player = Player.objects.filter(player_no=form.data['player_no']).first()
 #             log.player = player
 #             log.save()
 #             return redirect('log_detail', pk=log.pk)
 #     else:
 #         form = LogForm(instance=log)
 #     return render(request, 'penaltylogger/log_confirm.html', {'form': form})
# def log_confirm(request): #投稿確認画面（プレビュー）を表示
 #     if request.method == "POST":
 #         form = LogForm(request.POST)
 #         if form.is_valid():
 #             context = {'form': form }
 #             return render(request, "penaltylogger/log_save.html", context=context )
 #     else:
 #         form = LogForm()
 #     return render(request, 'penaltylogger/log_confirm.html', {'form': form})