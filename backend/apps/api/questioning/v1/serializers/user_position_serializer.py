from apps.api.auth.models import UserPosition
from apps.api.auth.v1.serializers import UserDataSerializers
from apps.api.reference.v1.serializers import (
    DepartmentSerializer,
    PositionSerializer,
)
from rest_framework import serializers


class UserPositionSerializer(serializers.ModelSerializer):
    """
    Должность пользователя
    """

    department = DepartmentSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    user = UserDataSerializers(read_only=True)

    class Meta:
        model = UserPosition
        fields = "__all__"
