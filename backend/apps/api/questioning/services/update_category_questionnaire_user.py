from django import forms
from service_objects.services import Service


class UpdateCategoryQuestionnaireUser(Service):
    """
    Обвновление данных по в категории анкеты пользователя
    """

    pk_category = forms.IntegerField()
    result_point_fixed = forms.FloatField()
    is_verified = forms.BooleanField()

    def process(self):
        pk_category = self.cleaned_data["pk_category"]
        result_point_fixed = self.cleaned_data["result_point_fixed"]
        is_verified = self.cleaned_data["is_verified"]
