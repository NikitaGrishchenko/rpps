from apps.api.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserDataSerializers(ModelSerializer):
    """ Сериализатор главной информации о пользователе пользователя """

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "patronymic",
            "last_name",
        ]
