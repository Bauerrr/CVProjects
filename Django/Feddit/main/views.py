from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    posts = models.Post.objects.all()
    context_list = {'posts': posts}
    return render(request, 'main/index.html', context=context_list)
