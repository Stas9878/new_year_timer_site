from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver

# class UserWish(models.Model):
#     author = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     def __str__(self):
#         return f'{self.name}'

class Wish(models.Model):
    wish = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='wish')
    publish = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.wish

#Для автоматического добавления юзера в User и в UserWish
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserWish.objects.create(name=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userwish.save()