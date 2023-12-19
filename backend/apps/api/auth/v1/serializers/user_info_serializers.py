from apps.api.auth.models import User
from apps.core.utils.fields import Base64Image
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .user_position_serializers import UserPositionSerializers


class UserInfoSerializers(WritableNestedModelSerializer):
    """ Информация о пользователе """

    user_image = Base64Image(represent_in_base64=True, allow_null=True)
    user_positions = UserPositionSerializers(many=True)

    class Meta:
        model = User
        fields = [
            "user_image",
            "user_positions",
        ]
