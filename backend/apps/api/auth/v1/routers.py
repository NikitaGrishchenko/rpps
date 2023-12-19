from django.conf.urls import include
from django.urls import path

from .views import (
    ApplicationSubmissionCreateAPIView,
    CheckExistUsernameAPIView,
    UserAPIListCreate,
    UserData,
    UserInfoAPIRetrieveUpdate,
    UserPositionList,
)

app_name = "auth"

# https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
# эндпоинты для авторизации

urlpatterns = [
    path("token/", include("dj_rest_auth.urls")),
    path("user/data/", UserData.as_view()),
    path("user-info/", UserInfoAPIRetrieveUpdate.as_view()),
    path("create-user/", UserAPIListCreate.as_view(), name="create-user"),
    path("user-position/", UserPositionList.as_view()),
    path(
        "application-submission/", ApplicationSubmissionCreateAPIView.as_view()
    ),
    path("check-username/", CheckExistUsernameAPIView.as_view()),
]
