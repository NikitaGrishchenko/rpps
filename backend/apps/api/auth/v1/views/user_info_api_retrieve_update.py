from apps.api.auth.models import User
from apps.api.auth.v1.serializers import UserInfoSerializers
from rest_framework.generics import RetrieveUpdateAPIView


class UserInfoAPIRetrieveUpdate(RetrieveUpdateAPIView):
    """ Редактирование информации о пользователе """

    serializer_class = UserInfoSerializers
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
