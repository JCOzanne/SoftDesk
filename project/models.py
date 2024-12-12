from django.conf import settings
from django.db import models

from config.settings import AUTH_USER_MODEL


class Project(models.Model):

    BACK_END = 'BACK_END'
    FRONT_END = 'FRONT_END'
    IOS = 'IOS'
    ANDROID = 'ANDROID'

    TYPE_CHOICES = [
        (BACK_END, 'back-end'),
        (FRONT_END, 'front-end'),
        (IOS, 'IOS'),
        (ANDROID, 'Android'),
    ]
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Type')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='author')

    def __str__(self):
        return f"{self.name} <{self.author}>"

class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')