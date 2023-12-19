from apps.api.reference.enums import TYPE_CATEGORY

from .base_choice_view import BaseChoiceView


class TypeCategoryList(BaseChoiceView):
    """
    Типы полей (список)
    """

    objects = TYPE_CATEGORY
