from apps.api.reference.models import Department
from rest_framework import serializers


class DepartmentNameSerializer(serializers.ModelSerializer):
    """ Наименование Кафедра """

    class Meta:
        model = Department
        fields = [
            "name",
        ]
