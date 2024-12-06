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