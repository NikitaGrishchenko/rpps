from apps.api.auth.models import UserPosition
from apps.api.auth.v1.serializers import UserPositionListSerializers
from rest_framework.generics import ListAPIView


class UserPositionList(ListAPIView):
    """ Список всех анкет пользователей """

    serializer_class = UserPositionListSerializers

    def get_queryset(self):
        return (
            UserPosition.objects.select_related(
                "user", "department__faculty", "rate", "position",
            )
            .prefetch_related("questionnaire_user__questionnaire")
            .all()
        )
