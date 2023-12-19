from apps.api.reference.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    """ Кафедра """

    class Meta:
        model = Department
        fields = "__all__"
        depth = 1
