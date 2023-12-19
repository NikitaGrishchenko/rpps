from apps.api.auth.models import User
from apps.api.auth.v1.serializers import UserCreateSerializer
from rest_framework.generics import CreateAPIView


class UserAPIListCreate(CreateAPIView):
    """ Cоздание пользователя """

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
