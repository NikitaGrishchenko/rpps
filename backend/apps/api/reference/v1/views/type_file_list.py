from apps.api.reference.enums import TYPE_FILE

from .base_choice_view import BaseChoiceView


class TypeFileList(BaseChoiceView):
    """
    Типы файлов (список)
    """

    objects = TYPE_FILE
