from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage
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
            return JsonResponse({'status' : 200}) #обязательно передать какой нибудь параметр
        else:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])#редирект на эту же страницу
        
    return render(request,'index/add_wish.html', context={'form': form})


def wishes(request):
    data = Wish.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)
    posts_data = paginator.get_page(page_number)

    return render(request, 'index/wishes.html', context={
        'data': posts_data,
    })

