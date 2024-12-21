from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from project.models import Project, Contributor, Issue, Comment
from user.serializers import UserSerializer


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = [
            'user',
            'project',
        ]

    def validate(self, data):
        project = data.get('project')
        user = data.get('user')

        if project.contributor.filter(id=user.id).exists():
            raise ValidationError(
                {"user": "Cet utilisateur est déjà un contributeur du projet"}
            )

        return data


class IssueDetailSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    in_charge = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = [
            'id',
            'name',
            'description',
            'date_created',
            'priority',
            'tag',
            'status',
            'project',
            'in_charge',
            'author',
        ]


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'name',
            'description',
            'date_created',
            'priority',
            'tag',
            'status',
            'project',
        ]


class ProjectDetailSerializer(ModelSerializer):
    issues = IssueListSerializer(many=True)
    contributor = UserSerializer(many=True, read_only=True)

    class Meta:

        model = Project
        fields = [
            'id',
            'name',
            'description',
            'type',
            'date_created',
            'author',
            'contributor',
            'issues',
            'contributor',
        ]


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'type',
            'author'
        ]
        read_only_fields = ["author"]


class CommentDetailSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:

        model = Comment
        fields = [
            'description',
            'date_created',
            'issue',
            'id',
            'author',
        ]


class CommentListSerializer(ModelSerializer):

    class Meta:

        model = Comment
        fields = [
            'description',
            'date_created',
            'issue',
            'id',
            'author',
        ]
        read_only_fields = ['author']
