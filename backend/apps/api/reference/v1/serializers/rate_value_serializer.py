from apps.api.reference.models import Rate
from rest_framework import serializers


class RateValueSerializer(serializers.ModelSerializer):
    """ Наименование Ставки """

    class Meta:
        model = Rate
        fields = [
            "value",
        ]
