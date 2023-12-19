import os

from config.settings.components.paths import LOGS_DIR
from django import forms
from loguru import logger
from service_objects.services import Service

LOG_FILE = os.path.join(LOGS_DIR, "{time:DD-MM-YYYY}.log")


class LoggingChangesInUserCategories(Service):
    """ Сервис для логгирования изменений в катериях анкеты пользователя """

    current_user = forms.CharField()
    questionnaire_user = forms.CharField()
    questionnaire = forms.CharField()
    category = forms.CharField()
    number_category = forms.CharField()

    logger.add(
        LOG_FILE,
        format="{time:HH:mm:ss} {level} {message}",
        level="INFO",
        rotation="00:00",
        compression="zip",
        enqueue=True,
    )

    def process(self):

        current_user = self.cleaned_data["current_user"]
        questionnaire_user = self.cleaned_data["questionnaire_user"]
        category = self.cleaned_data["category"]
        questionnaire = self.cleaned_data["questionnaire"]
        number_category = self.cleaned_data["number_category"]

        logger.info(
            f"{current_user} made changes to {questionnaire_user} ({questionnaire}) в {category} (number: {number_category})"
        )

