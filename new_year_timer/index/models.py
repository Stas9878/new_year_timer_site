from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Wish(models.Model):
    wish = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='wish')
    publish = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.wish
