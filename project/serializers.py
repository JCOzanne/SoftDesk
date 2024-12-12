from rest_framework.serializers import ModelSerializer
from project.models import Project, Contributor

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'type'
            'date_created',
            'author'
            'contributor'
        ]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            'user',
            'project',
        ]