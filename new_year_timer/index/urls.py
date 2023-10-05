from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('dream/', dream, name='dream',),
    path('login/', login, name='login'),
    ]
