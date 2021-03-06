from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'personal/home.html', {
        'posts': posts,
        'nbar': 'home',
        })

def adaptive(request):
    return render(request, 'personal/adaptive.html', {'nbar': 'adaptive'})
