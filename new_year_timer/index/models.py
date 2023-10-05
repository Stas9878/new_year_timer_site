from django.db import models

class UserWish(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

class Wish(models.Model):
    wish = models.CharField(max_length=200)
    author = models.ForeignKey(UserWish, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.wish