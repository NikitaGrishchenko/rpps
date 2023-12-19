from apps.api.reference.models import Position
from rest_framework import serializers


class PositionSerializer(serializers.ModelSerializer):
    """ Должности """

    class Meta:
        model = Position
        fields = "__all__"
