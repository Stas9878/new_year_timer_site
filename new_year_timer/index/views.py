from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserWish
from .forms import *

def index(request):
    return render(request, 'index/index.html')

def add_wish(request):
    form = MakeWIshForm()
    if request.method == 'POST':
        data = {
            'wish': request.POST['wish'],
            'author': None
            
        }
        if request.user.is_authenticated:
            data['author'] = request.user.id

        form = MakeWIshForm(data=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        
    return render(request,'index/add_wish.html', context={'form': form})


def wishes(request):
    pass

def login(request):
    pass