from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Log
from .models import Player
from .forms import LogForm
from . import forms


def post_list(request):
    return render(request, 'penaltylogger/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Log, pk=pk)
    return render(request, 'penaltylogger/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = LogForm()
    return render(request, 'penaltylogger/post_log.html', {'form': form})

def post_log(request, pk):
    post = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=post)
        if form.is_valid():
            log = form.save(commit=False)
            player = Player.objects.filter(player_no=form.player_no).first()
            log.player = player
            log.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = LogForm(instance=post)
    return render(request, 'penaltylogger/post_log.html', {'form': form})