from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('add-wish/', add_wish, name='add-wish'),
    path('wishes/', wishes, name='wishes',),
    ]
