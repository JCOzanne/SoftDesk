from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from project.models import Project, Contributor, Issue, Comment
from project.serializers import ProjectDetailSerializer, ContributorSerializer, ProjectListSerializer, \
    IssueListSerializer, IssueDetailSerializer, CommentDetailSerializer, CommentListSerializer


class MultipleSerializerMixin :

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve'and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()
