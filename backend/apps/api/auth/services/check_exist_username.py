# from apps.api.auth.models import UserPosition
# from apps.api.questioning.models import QuestionnaireUser
from apps.api.auth.models import UserPosition
from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from service_objects.fields import ListField
from service_objects.services import Service


class CheckExistUsername(Service):
    """
    The service of checking is exist a username
    during registration
    Arguments:
      username: string
    Returns:
      is_exist: boolean
    """

    username = forms.CharField()

    def process(self):
        username = self.cleaned_data["username"]
        User = get_user_model()

        try:
            user = User.objects.get(username=username)
            if user:
                is_exist = True
        except User.DoesNotExist:
            is_exist = False

        return is_exist

