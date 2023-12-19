# from apps.api.auth.models import UserPosition
# from apps.api.questioning.models import QuestionnaireUser
from apps.api.auth.models import UserPosition
from django import forms
from django.contrib.auth import get_user_model
from service_objects.fields import ListField
from service_objects.services import Service


class CreateUserAndUserPosition(Service):
    """ Сервис для создания пользователя и должностей пользователя """

    username = forms.CharField()
    password = forms.CharField()

    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)

    user_image = forms.ImageField(required=False)

    user_positions = ListField(required=False)

    def process(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        user_image = self.cleaned_data["user_image"]

        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        patronymic = self.cleaned_data["patronymic"]

        user_positions = self.cleaned_data["user_positions"]

        # создание пользователя
        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        if patronymic:
            user.patronymic = patronymic
        if user_image:
            user.user_image = user_image

        user.save()

        # создания должностей пользователя
        if user_positions:
            for item in user_positions:
                UserPosition.objects.create(user=user, **item)
        return user

