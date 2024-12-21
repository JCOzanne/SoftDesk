from rest_framework.permissions import BasePermission

from project.models import Project, Issue, Comment


class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Project):
            return obj.contributor.filter(id=request.user.id).exists()
        elif isinstance(obj, Issue) or isinstance(obj, Comment):
            return obj.issue.project.contributor.filter(id=request.user.id).exists()
        return False


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        return True
