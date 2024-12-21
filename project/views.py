from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from project.models import Project, Contributor, Issue, Comment
from project.permissions import IsProjectContributor, IsAuthorOrReadOnly
from project.serializers import ProjectDetailSerializer, ContributorSerializer, ProjectListSerializer, \
    IssueListSerializer, IssueDetailSerializer, CommentDetailSerializer, CommentListSerializer
from user.models import User


class MultipleSerializerMixin :

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve'and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        project.contributor.add(self.request.user)


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        return Contributor.objects.all()

    def perform_create(self, serializer):
        project = serializer.validated_data.get('project')
        user = serializer.validated_data.get('user')

        if not project.contributor.filter(id=user.id).exists():
            project.contributor.add(user)
            project.save()
        else:
            raise ValidationError(
                {"user": "Cet utilisateur est déjà un contributeur du projet"}
            )

        serializer.save()


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Issue.objects.all()

    def perform_create(self, serializer):
        project = serializer.validated_data.get('project')
        in_charge_id = self.request.data.get('in_charge')
        if in_charge_id:
            if not project.contributor.filter(id=in_charge_id).exists():
                raise ValidationError(
                    {"in_charge": "L'utilisateur assigné doit être un contributeur du projet"}
                )
            in_charge = User.objects.get(id=in_charge_id)
        else:
            in_charge = self.request.user

        serializer.save(
            author=self.request.user,
            in_charge=in_charge
        )

    def perform_update(self, serializer):
        in_charge_id = self.request.data.get('in_charge')
        if in_charge_id:
            project = serializer.instance.project
            if not project.contributor.filter(id=in_charge_id).exists():
                raise ValidationError(
                    {"in_charge": "L'utilisateur assigné doit être un contributeur du projet"}
                )
            in_charge = User.objects.get(id=in_charge_id)
            serializer.save(in_charge=in_charge)
        else:
            serializer.save()


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        issue = serializer.validated_data.get('issue')
        if not issue.project.contributor.filter(id=self.request.user.id).exists():
            raise ValidationError(
                {"issue": "Vous devez être un contributeur du projet pour commenter cette issue"}
            )
        serializer.save(author=self.request.user)
