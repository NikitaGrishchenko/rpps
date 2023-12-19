from apps.api.reference.models import Department
from rest_framework import serializers

from .user_position_department_serializers import (
    UserPositionDepartmentSerializers,
)


class DepartmentDetailSerializer(serializers.ModelSerializer):
    """ Кафедра (подробно)"""

    user_positions = UserPositionDepartmentSerializers(
        many=True, read_only=True
    )

    class Meta:
        model = Department
        fields = "__all__"
