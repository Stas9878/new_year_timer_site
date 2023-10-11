from django.shortcuts import render


def register(request):
    pass


def login(request):
    return render(request, 'accounts/login.html')


