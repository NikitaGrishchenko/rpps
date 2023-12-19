from apps.api.auth.models import User
from rest_framework import serializers


class UserUsernameSerializers(serializers.Serializer):
    """ Сериализатор главной информации о пользователе пользователя """

    username = serializers.CharField()

