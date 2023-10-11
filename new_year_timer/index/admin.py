from django.contrib import admin
from .models import *

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ['wish','author', 'publish','id']
 
# @admin.register(UserWish)
# class WishAdmin(admin.ModelAdmin):
#     list_display = ['name','id']

