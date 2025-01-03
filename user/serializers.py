from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):

    """
    A serializer for the User model.
    Handles serialization and validation of User data for API requests and responses.
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'age_min',
            'can_be_contacted',
            'data_can_be_shared',
        ]

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        """
        Creates a new User object with the provided validated data.
        :param validated_data:
        :return: The newly created user instance.
        """
        user = User.objects.create_user(**validated_data)
        return user
