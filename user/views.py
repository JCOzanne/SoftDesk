from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()