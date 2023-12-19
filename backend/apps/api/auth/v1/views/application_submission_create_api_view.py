from apps.api.auth.models import ApplicationSubmission
from apps.api.auth.v1.serializers import ApplicationSubmissionSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class ApplicationSubmissionCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ApplicationSubmissionSerializer
    queryset = ApplicationSubmission
