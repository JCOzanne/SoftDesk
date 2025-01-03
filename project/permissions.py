from typing import Any

from django.http import HttpRequest
from rest_framework.permissions import BasePermission

from project.models import Project, Issue, Comment


class IsProjectContributor(BasePermission):

    def has_permission(self, request: HttpRequest, view) -> bool:

        """
        Checks whether the requesting user has general permission to access the given
        :param request: The HTTP request being processed.
        :param view: The Django REST Framework view handling the request.
        :return: True if the user has permission to access the view, False otherwise.
        """

        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request: HttpRequest, view, obj: Any) -> bool:

        """
        Checks whether the requesting user has permission to perform the requested action
        on a specific object.
        :param request: The HTTP request being processed.
        :param view: The Django REST Framework view handling the request.
        :param obj: The object on which the permission check is being performed.
        :return: True if the user has permission to access the object, False otherwise.
        """

        if isinstance(obj, Project):
            return obj.contributor.filter(id=request.user.id).exists()
        elif isinstance(obj, Issue):
            return obj.project.contributor.filter(id=request.user.id).exists()
        elif isinstance(obj, Comment):
            return obj.issue.project.contributor.filter(id=request.user.id).exists()
        return False


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        return True
