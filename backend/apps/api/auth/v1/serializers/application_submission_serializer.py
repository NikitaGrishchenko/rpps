from apps.api.auth.models import (
    ApplicationSubmission,
    ApplicationSubmissionPosition,
)
from apps.api.auth.v1.serializers import (
    ApplicationSubmissionPositionSerializer,
)
from rest_framework.serializers import ModelSerializer


class ApplicationSubmissionSerializer(ModelSerializer):
    """ Сериализатор подачи заявки на регистрацию """

    application_submission_position = ApplicationSubmissionPositionSerializer(
        many=True
    )

    class Meta:
        model = ApplicationSubmission
        fields = [
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "application_submission_position",
        ]

    def create(self, validated_data):
        application_submission_position = validated_data.pop(
            "application_submission_position"
        )
        application_submission = ApplicationSubmission.objects.create(
            **validated_data
        )

        for item in application_submission_position:
            ApplicationSubmissionPosition.objects.create(
                application_submission=application_submission, **item
            )

        return application_submission
