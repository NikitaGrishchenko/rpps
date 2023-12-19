from apps.api.reference.models import Department
from apps.api.reference.v1.serializers import DepartmentSerializer
from rest_framework import generics


class DepartmentAPIRetrieve(generics.RetrieveAPIView):
    """
    Кафедра
    """

    lookup_url_kwarg = "pk_department"
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
