from apps.api.reference.models import Faculty
from apps.api.reference.v1.serializers import FacultySerializer
from rest_framework import generics


class FacultyAPIList(generics.ListAPIView):
    """
    Справочник факультетов
    """

    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
