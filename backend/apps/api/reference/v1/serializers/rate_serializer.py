from apps.api.reference.models import Rate
from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    """ Ставки """

    class Meta:
        model = Rate
        fields = "__all__"
