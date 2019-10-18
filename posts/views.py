from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request):
  #return HttpResponse('HELLO FROM POSTS')

  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)
