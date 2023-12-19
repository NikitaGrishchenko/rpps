from apps.api.auth.models import UserPosition
from rest_framework.serializers import ModelSerializer


class UserPositionSerializers(ModelSerializer):
    """ Должности пользователя """

    class Meta:
        model = UserPosition
        fields = "__all__"
