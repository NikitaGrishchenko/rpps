from apps.api.auth.models import UserFile
from rest_framework.serializers import ModelSerializer


class UserFileSerializers(ModelSerializer):
    """ Сериализатор файлов пользователя """

    class Meta:
        model = UserFile
        fields = "__all__"
