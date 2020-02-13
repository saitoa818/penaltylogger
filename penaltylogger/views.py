from django.shortcuts import render
from django.utils import timezone
from .models import Log
from django.shortcuts import render, get_object_or_404
from .forms import LogForm

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
    return render(request, 'penaltylogger/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.Log, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = LogForm(instance=post)
    return render(request, 'penaltylogger/post_edit.html', {'form': form})