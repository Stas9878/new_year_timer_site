from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')

def add_wish(request):
    if request.method == 'GET':
        return render(request,'index/add_wish.html' )

def wishes(request):
    pass

def login(request):
    pass