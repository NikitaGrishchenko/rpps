from apps.api.reference.models import Position
from rest_framework import serializers


class PositionNameSerializer(serializers.ModelSerializer):
    """ Наименование Должности """

    class Meta:
        model = Position
        fields = [
            "name",
        ]
