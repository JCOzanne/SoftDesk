from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):

    """
    A viewset for managing User objects.
    Provides CRUD operations for users with appropriate permissions.
    """

    serializer_class = UserSerializer

    def get_queryset(self) -> QuerySet[User]:

        """
        Retrieves all User objects from the database.
        :return: A queryset containing all users.
        """
        return User.objects.all()
