# import json


from django import forms
from service_objects.services import Service

from .average_by_main_category import average_by_main_category
from .average_score_for_sections_in_each_faculty import (
    average_score_for_sections_in_each_faculty,
)
from .count_of_teachers import count_of_teachers
from .count_of_teachers_scored_above_average import (
    count_of_teachers_scored_above_average,
)
from .count_of_teachers_scored_lower_average import (
    count_of_teachers_scored_lower_average,
)
from .get_queryset import get_queryset
from .list_info_about_users_and_departaments import (
    list_info_about_users_and_departaments,
)
from .rating_faculty import rating_faculty
from .top_departments import top_departments
from .top_teachers_by_university import top_teachers_by_university
from .top_teachers_in_each_category import top_teachers_in_each_category
from .total_average_score import total_average_score
from .total_score_of_all_users import total_score_of_all_users

# from django.contrib.auth import get_user_model


class QuestionnaireStatistics(Service):
    """ сервис для получения статистики по определенной анкете """

    questionnaire_id = forms.IntegerField()

    def process(self):
        """ Главная функция. """

        # получаем id анкеты для сортировки данных
        questionnaire_id = self.cleaned_data["questionnaire_id"]

        # выборка данных для определенной анкеты
        queryset = get_queryset(questionnaire_id)

        # формирование списка всех данных, для использования дальше
        data = list_info_about_users_and_departaments(queryset)

        result_data = []

        result_data.append(
            {
                "tableName": "Общая информация",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "value", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": "Количество пользователей у которых значение > 0",
                        "value": count_of_teachers(data),
                        "order": 1,
                    },
                    {
                        "name": "Общий балл",
                        "value": total_score_of_all_users(data),
                        "order": 2,
                    },
                    {
                        "name": "Средний балл на одного человека",
                        "value": total_average_score(data),
                        "order": 3,
                    },
                ],
            }
        )

        # Средний балл по главным категориям и в общем
        current_data = average_by_main_category(data)
        result_data.append(
            {
                "tableName": "Средний балл по главным категориям",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "value", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Количество преподавателей, набравших баллы выше среднего
        current_data = count_of_teachers_scored_above_average(data)
        result_data.append(
            {
                "tableName": "Количество преподавателей, набравших баллы выше среднего",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "countUsers", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "count_users": item["count_users"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Количество преподавателей, набравших баллы ниже среднего
        current_data = count_of_teachers_scored_lower_average(data)
        result_data.append(
            {
                "tableName": "Количество преподавателей, набравших баллы ниже среднего",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "countUsers", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "count_users": item["count_users"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Рейтинг по факультетам
        current_data = rating_faculty(data)
        result_data.append(
            {
                "tableName": "Рейтинг факультетов",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "value", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Топ преподавателей
        current_data = top_teachers_by_university(data, 10)
        result_data.append(
            {
                "tableName": "Топ 10 преподавателей",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "faculty", "label": "Факультет",},
                    {"name": "department", "label": "Кафедра",},
                    {"name": "value", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "faculty": item["faculty"],
                        "department": item["department"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Топ кафедр
        current_data = top_departments(data)
        result_data.append(
            {
                "tableName": "Топ кафедр",
                "columns": [
                    {"name": "name", "label": "Наименование",},
                    {"name": "value", "label": "Значение",},
                ],
                "rows": [
                    {
                        "name": item["name"],
                        "value": item["points"],
                        "order": index,
                    }
                    for index, item in enumerate(current_data)
                ],
            }
        )

        # Средний балл по разделам в каждом факультете
        current_data = average_score_for_sections_in_each_faculty(data)
        result_data.append(
            {
                "tableName": "Средний балл по разделам в каждом факультете",
                "nested": [
                    {
                        "columns": [
                            {
                                "name": "nameDirection",
                                "label": "Наименование раздела",
                            },
                            {"name": "nameDepartment", "label": "Кафедра",},
                            {"name": "value", "label": "Значение",},
                        ],
                        "rows": [
                            {
                                "nameDirection": item["name"],
                                "nameDepartment": nested_item["name"],
                                "value": nested_item["points"],
                                "order": index,
                            }
                            for index, nested_item in enumerate(
                                item["faculties"]
                            )
                        ],
                    }
                    for item in current_data
                ],
            }
        )

        # # топ преподов в каждой главной категории
        current_data = top_teachers_in_each_category(data, 10)
        result_data.append(
            {
                "tableName": "Топ преподовавателей в главных категориях",
                "nested": [
                    {
                        "columns": [
                            {
                                "name": "nameDirection",
                                "label": "Наименование раздела",
                            },
                            {"name": "nameUser", "label": "Пользователь",},
                            {"name": "faculty", "label": "Факультет",},
                            {"name": "department", "label": "Кафедра",},
                            {"name": "value", "label": "Значение",},
                        ],
                        "rows": [
                            {
                                "nameDirection": item["name"],
                                "nameUser": nested_item["name"],
                                "faculty": nested_item["faculty"],
                                "department": nested_item["department"],
                                "value": nested_item["points"],
                                "order": index,
                            }
                            for index, nested_item in enumerate(item["users"])
                        ],
                    }
                    for item in current_data
                ],
            }
        )

        return result_data
