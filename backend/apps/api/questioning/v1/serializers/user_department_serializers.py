from apps.api.auth.models import User
from rest_framework import serializers


class UserDepartmentSerializers(serializers.ModelSerializer):
    """ Сотрудник """

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "patronymic",
        ]
