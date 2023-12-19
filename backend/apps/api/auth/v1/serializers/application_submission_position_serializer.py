from apps.api.auth.models import ApplicationSubmissionPosition
from rest_framework.serializers import ModelSerializer


class ApplicationSubmissionPositionSerializer(ModelSerializer):
    """ Сериализатор должности пользователя при подачи заявки на регистрацию"""

    class Meta:
        model = ApplicationSubmissionPosition
        fields = "__all__"
