from apps.api.auth.models import UserPosition
from apps.api.auth.v1.serializers import UserDataSerializers
from apps.api.questioning.v1.serializers import (
    QuestionnaireUserListAPISerializer,
)
from apps.api.reference.v1.serializers import (
    DepartmentNameSerializer,
    PositionNameSerializer,
    RateValueSerializer,
)
from rest_framework.serializers import ModelSerializer


class UserPositionListSerializers(ModelSerializer):
    """ Должности пользователя подробный список"""

    user = UserDataSerializers(read_only=True)
    rate = RateValueSerializer(read_only=True)
    department = DepartmentNameSerializer(read_only=True)
    position = PositionNameSerializer(read_only=True)
    questionnaire_user = QuestionnaireUserListAPISerializer(
        many=True, read_only=True
    )

    class Meta:
        model = UserPosition
        fields = "__all__"
