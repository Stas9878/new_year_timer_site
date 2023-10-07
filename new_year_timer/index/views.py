from django.shortcuts import render,HttpResponseRedirect
from .forms import *

def index(request):
    return render(request, 'index/index.html')

def add_wish(request):
    form = MakeWIshForm()
    if request.method == 'POST':
        form = MakeWIshForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
        
    return render(request,'index/add_wish.html', context={'form': form})


def wishes(request):
    pass

def login(request):
    pass