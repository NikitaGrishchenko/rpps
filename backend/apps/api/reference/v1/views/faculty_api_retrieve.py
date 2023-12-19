from apps.api.reference.models import Faculty
from apps.api.reference.v1.serializers import FacultySerializer
from rest_framework import generics


class FacultyAPIRetrieve(generics.RetrieveAPIView):
    """
    Справочник факультетов
    """

    lookup_url_kwarg = "pk_faculty"
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
