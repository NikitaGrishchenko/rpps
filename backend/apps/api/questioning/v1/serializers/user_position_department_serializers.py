from apps.api.auth.models import UserPosition
from apps.api.reference.v1.serializers import PositionSerializer
from rest_framework import serializers

from .questionnaire_user_department_serializer import (
    QuestionnaireUserDepartmentSerializer,
)
from .user_department_serializers import UserDepartmentSerializers


class UserPositionDepartmentSerializers(serializers.ModelSerializer):
    """ Сотрудники кафедры"""

    user = UserDepartmentSerializers(read_only=True)
    position = PositionSerializer(read_only=True)

    questionnaire_user = QuestionnaireUserDepartmentSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = UserPosition
        fields = "__all__"
