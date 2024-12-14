from rest_framework.serializers import ModelSerializer
from user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'password',
            'age_min',
            'can_be_contacted',
            'data_can_be_shared',
        ]

        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user