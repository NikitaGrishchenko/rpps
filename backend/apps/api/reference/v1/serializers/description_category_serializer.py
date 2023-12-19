from apps.api.reference.models import DescriptionCategory
from rest_framework import serializers


class DescriptionCategorySerializer(serializers.ModelSerializer):
    """ Описание категории """

    class Meta:
        model = DescriptionCategory
        fields = "__all__"
