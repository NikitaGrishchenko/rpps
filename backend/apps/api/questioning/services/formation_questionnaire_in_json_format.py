from apps.api.questioning.models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
    MainCategoryQuestionnaire,
    MainCategoryQuestionnaireUser,
    QuestionnaireUser,
)

# from apps.api.reference.models import Faculty
from django import forms
from service_objects.services import Service


class FormationQuestionnaireInJsonFormat(Service):
    """
    Сервис для формирования анкеты в json формат
    для удобного вывода на клиенте:
    1. Формирование самой анкеты
    2. Замена категорий анеты на категории анкеты пользователя
    """

    questionnaire_user_id = forms.IntegerField()

    _category_questionnaire_queryset = None
    _category_questionnaire_user_queryset = None
    _main_category_questionnaire_queryset = None
    _main_category_questionnaire_user_queryset = None
    _questionnaire_user_queryset = None

    def process(self):
        questionnaire_user_id = self.cleaned_data["questionnaire_user_id"]
        result = {}

        self._init_related_querysets()

        # получаем текущую анкету пользователя
        questionnaire_user = self._questionnaire_user_queryset.get(
            id=questionnaire_user_id
        )

        # получаем главные категории анкеты
        main_categories = self._main_category_questionnaire_queryset.filter(
            questionnaire=questionnaire_user.questionnaire
        )
        # добавляем в результирующий массив главные категории анкеты
        for main_category in main_categories:
            dict_main_category = {
                "id": main_category.id,
                "number": main_category.number,
                "name": main_category.reference_category.name,
                "id_reference_category": main_category.reference_category.id,
            }
            result[
                f"categoryNumber:{main_category.number}"
            ] = dict_main_category

        # получаем категории анкеты со всеми вложенными категориями
        #  для каждой главной категории
        #  и добавляем к главной
        for key, item in result.items():
            categories_questionnaire = self._category_questionnaire_queryset.filter(
                main_category__questionnaire=questionnaire_user.questionnaire,
                main_category__id=item["id"],
            )
            result[key]["category"] = self._get_nested_category(
                categories_questionnaire
            )

        return self._replacing_categories(result)

    def _init_related_querysets(self):
        self._category_questionnaire_queryset = (
            CategoryQuestionnaire.objects.select_related(
                "reference_category__description",
                "periodicity",
                "rating",
            )
        )
        self._questionnaire_user_queryset = (
            QuestionnaireUser.objects.select_related(
                "questionnaire",
            )
        )
        self._category_questionnaire_user_queryset = (
            CategoryQuestionnaireUser.objects
        )
        self._main_category_questionnaire_queryset = (
            MainCategoryQuestionnaire.objects.select_related(
                "reference_category",
            )
        )
        self._main_category_questionnaire_user_queryset = (
            MainCategoryQuestionnaireUser.objects
        )

    def _replacing_categories(self, result):
        """
        Замена категории анкеты на категории анкеты пользователя
        """
        questionnaire_user_id = self.cleaned_data["questionnaire_user_id"]

        for key_main_category, item_main_category in result.items():
            try:
                main_category_questionnair_user = (
                    self._main_category_questionnaire_user_queryset.get(
                        questionnaire_user__id=questionnaire_user_id,
                        main_category_questionnaire__id=item_main_category[
                            "id"
                        ],
                    )
                )
                item_main_category["id"] = main_category_questionnair_user.id
                item_main_category["result_point"] = self._get_round_number(
                    main_category_questionnair_user.result_point
                )
                item_main_category[
                    "result_point_fixed"
                ] = self._get_round_number(
                    main_category_questionnair_user.result_point_fixed
                )
            except MainCategoryQuestionnaireUser.DoesNotExist:
                pass
            for key_category, item_category in item_main_category[
                "category"
            ].items():
                try:
                    category_questionnaire_user = (
                        self._category_questionnaire_user_queryset.get(
                            category_questionnaire__id=item_category["id"],
                            questionnaire_user__id=questionnaire_user_id,
                        )
                    )
                    item_category["id"] = category_questionnaire_user.id
                    item_category["result_point"] = self._get_round_number(
                        category_questionnaire_user.result_point
                    )
                    item_category[
                        "result_point_fixed"
                    ] = self._get_round_number(
                        category_questionnaire_user.result_point_fixed
                    )
                    item_category["count_files"] = self._getCountAttachedFiles(
                        category_questionnaire_user.id
                    )
                    item_category[
                        "is_verified"
                    ] = category_questionnaire_user.is_verified

                except CategoryQuestionnaireUser.DoesNotExist:
                    pass

        result = self._sort_categories_by_number(result)

        return result

    def _sort_categories_by_number(self, questionnaire: dict):
        """
        Функция сортировки словаря анкеты по полю number
        и всем вложеным подкатегориям
        Параметры:
            questionnaire (dict): анкета пользователя
        Возвращаемое значение:
            sorted_result (dict): отсортированная анкета пользователя
        """

        return {
            category_key: {
                "category": self._sort_categories_by_number(
                    category_value.pop("category")
                ),
                **category_value,
            }
            if isinstance(category_value, dict)
            and "category" in category_value.keys()
            else category_value
            for category_key, category_value in sorted(
                questionnaire.items(),
                key=lambda category: list(
                    map(int, str(category[1]["number"]).split("."))
                ),
            )
        }

    def _get_nested_category(self, categories_questionnaire):
        """
        Формирование категорий со вложенной структурой
        """
        categories = {}
        # обработка первого уровня вложенности
        for category_questionnaire in categories_questionnaire:
            categories[f"categoryNumber:{category_questionnaire.id}"] = {
                "id": category_questionnaire.id,
                "number": f"{category_questionnaire.number}",
                "name": category_questionnaire.reference_category.name,
                "description": self._get_description_category(
                    category_questionnaire.reference_category.description
                ),
                "periodicity": self._get_periodicity_category(
                    category_questionnaire.periodicity
                ),
                "type_category": category_questionnaire.type_category,
                "rating": self._get_rating_category(
                    category_questionnaire.rating
                ),
                "weight": category_questionnaire.weight,
                "max_weight": category_questionnaire.max_weight,
                "use_internet_resource_link": category_questionnaire.use_internet_resource_link,
                "internet_resource_link_or_doc": category_questionnaire.internet_resource_link_or_doc,
                "nesting_level": 1,
            }
            # обработка второго уровня вложенности
            second_level_categories = (
                self._category_questionnaire_queryset.filter(
                    parent__id=category_questionnaire.id
                )
            )
            for second_level_category in second_level_categories:
                categories[f"categoryNumber:{second_level_category.id}"] = {
                    "id": second_level_category.id,
                    "number": f"{category_questionnaire.number}.{second_level_category.number}",
                    "name": second_level_category.reference_category.name,
                    "description": self._get_description_category(
                        second_level_category.reference_category.description
                    ),
                    "periodicity": self._get_periodicity_category(
                        second_level_category.periodicity
                    ),
                    "type_category": second_level_category.type_category,
                    "rating": self._get_rating_category(
                        second_level_category.rating
                    ),
                    "weight": second_level_category.weight,
                    "max_weight": second_level_category.max_weight,
                    "use_internet_resource_link": second_level_category.use_internet_resource_link,
                    "internet_resource_link_or_doc": second_level_category.internet_resource_link_or_doc,
                    "nesting_level": 2,
                }
                # обработка третьего уровня вложенности
                third_level_categories = (
                    self._category_questionnaire_queryset.filter(
                        parent__id=second_level_category.id
                    )
                )
                for third_level_category in third_level_categories:
                    categories[f"categoryNumber:{third_level_category.id}"] = {
                        "id": third_level_category.id,
                        "number": f"{category_questionnaire.number}.{second_level_category.number}.{third_level_category.number}",
                        "name": third_level_category.reference_category.name,
                        "description": self._get_description_category(
                            third_level_category.reference_category.description
                        ),
                        "periodicity": self._get_periodicity_category(
                            third_level_category.periodicity
                        ),
                        "type_category": third_level_category.type_category,
                        "rating": self._get_rating_category(
                            third_level_category.rating
                        ),
                        "weight": third_level_category.weight,
                        "max_weight": third_level_category.max_weight,
                        "use_internet_resource_link": third_level_category.use_internet_resource_link,
                        "internet_resource_link_or_doc": third_level_category.internet_resource_link_or_doc,
                        "nesting_level": 3,
                    }

        return categories

    def _getCountAttachedFiles(self, category_questionnaire_user: int) -> int:
        """
        Функция, которая возвращает количество прикрепленных
        файлов к категории анкеты пользователя
        Параметры:
            category_questionnaire_user (int): id анкеты пользователя
        Возвращаемое значение:
            count_files (int): количество файлов
        """

        count_files = FileCategoryQuestionnaireUser.objects.filter(
            category_questionnaire_id=category_questionnaire_user
        ).count()

        return count_files

    def _get_periodicity_category(self, obj):
        """
        Возвращает правильную переодичность категории анкеты
        """
        if obj is None:
            return None
        return obj.text

    def _get_rating_category(self, obj):
        """
        Возвращает правильный рейтинг категории анкеты
        """
        if obj is None:
            return None
        return obj.text

    def _get_description_category(self, obj):
        """
        Возвращает описание категории анкеты
        """
        if obj is None:
            return None
        return obj.text

    def _get_round_number(self, obj):
        """
        Возвращает округленное число, сперва проверяя на None
        """
        if obj is None:
            return None
        return round(obj, 2)
