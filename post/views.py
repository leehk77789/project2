from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def upload(request):
    if request.method == 'POST':
        post = Post()
        post.user = request.user
        post.image = request.FILES.get('img')
        
        post.save()

        return redirect('/users/main')