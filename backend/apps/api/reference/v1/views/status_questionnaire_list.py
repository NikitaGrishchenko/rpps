from apps.api.reference.enums import STATUS_QUESTIONARY

from .base_choice_view import BaseChoiceView


class StatusQuestionnaireList(BaseChoiceView):
    """
    Статусы анкет (список)
    """

    objects = STATUS_QUESTIONARY
