from apps.api.auth.services.check_exist_username import CheckExistUsername
from apps.api.auth.v1.serializers import UserUsernameSerializers
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckExistUsernameAPIView(APIView):
    """
    The api point of checking is exist a username
    during registration
    Arguments:
      username: string
    Returns:
      is_exist: boolean
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserUsernameSerializers(data=request.data)
        if serializer.is_valid():
            is_exist = CheckExistUsername.execute(
                {"username": serializer.validated_data.get("username")}
            )
            return Response({"is_exist": is_exist})

