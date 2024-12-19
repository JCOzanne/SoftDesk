from django.conf import settings
from django.db import models

import uuid

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
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'project_author')
    contributor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='project')

    def __str__(self):
        return f"{self.name} <{self.author}>"


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')


class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'
    TAG_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
        (TASK, 'Task'),
    ]

    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    FINISHED = 'FINISHED'
    STATUS_CHOICES = [
        (TODO, 'Todo'),
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, verbose_name='Type')
    tag = models.CharField(max_length=10, choices=TAG_CHOICES, verbose_name='Type')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Type')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    in_charge = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='in_charge')

    def __str__(self):
        return f"{self.name} <{self.in_charge}>"


class Comment(models.Model):
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
