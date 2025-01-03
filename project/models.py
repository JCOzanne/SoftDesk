from django.conf import settings
from django.db import models

import uuid

from config.settings import AUTH_USER_MODEL


class Project(models.Model):

    """
    Represents a project with related issues and contributors.
    Attributes:
        name (CharField): The name of the project.
        description (CharField): A detailed description of the project.
        type (CharField): The type of project (e.g., back-end, front-end, iOS, Android).
        date_created (DateTimeField): The timestamp when the project was created.
        author (ForeignKey): The user who created the project.
        contributor (ManyToManyField): The users who are contributors to the project.
    """

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
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_author')
    contributor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='project')

    def __str__(self):
        return f"{self.name} <{self.author}>"


class Contributor(models.Model):

    """
    Links a User to a Project as a contributor.
    Attributes:
        user (ForeignKey): The user contributing to the project.
        project (ForeignKey): The project the user contributes to.
    """

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')


class Issue(models.Model):

    """
    Represents an issue within a project.
    Attributes:
        name (CharField): The name of the issue.
        description (CharField): Details about the issue.
        priority (CharField): The priority level of the issue (e.g., Low, Medium, High).
        tag (CharField): The category of the issue (e.g., Bug, Feature, Task).
        status (CharField): The current status of the issue (e.g., To Do, In Progress, Finished).
        date_created (DateTimeField): The timestamp when the issue was created.
        author (ForeignKey): The user who reported the issue.
        project (ForeignKey): The project the issue belongs to.
        in_charge (ForeignKey): The user assigned to resolve the issue.
    """

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

    """
    Represents a comment on an issue.
    Attributes:
        description (CharField): The text of the comment.
        date_created (DateTimeField): The timestamp when the comment was created.
        author (ForeignKey): The user who wrote the comment.
        issue (ForeignKey): The issue the comment is associated with.
    """

    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
