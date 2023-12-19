from apps.api.reference.models import Category
from rest_framework import serializers

from .description_category_serializer import DescriptionCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    """ Категории """

    description = DescriptionCategorySerializer()

    class Meta:
        model = Category
        fields = "__all__"
