# from apps.api.auth.models import UserPosition
import itertools

from apps.api.questioning.models import CategoryQuestionnaireUser
from apps.api.reference.models import Faculty
from django import forms
from service_objects.services import Service


class StatisticsByCategory(Service):
    """ Сервис для получения статистики по категории анкеты пользователя """

    pk_category = forms.IntegerField()

    def process(self):

        pk_category = self.cleaned_data["pk_category"]

        data = Faculty.objects.all()

        faculties = self.list_by_faculties(data, pk_category)

        current_id = 0
        result_data = []

        # получение наименования категории
        # current_data = self.name_category(faculties)

        # result_data.append(
        #     {"id": current_id, "table": "zero", "name": current_data}
        # )

        # current_id += 1

        # кол-во преподов по факультетам
        current_data = self.count_users_in_faculties(faculties)

        for item in current_data:
            result_data.append(
                {
                    "id": current_id,
                    "table": "one",
                    "name": item["name"],
                    "value": item["count_users"],
                }
            )
            current_id += 1

        # топ 10 преподов
        current_data = self.top_users(faculties)

        for item in current_data:
            result_data.append(
                {
                    "id": current_id,
                    "table": "two",
                    "name": item["name"],
                    "value": item["points"],
                    "faculty": item["faculty"],
                    "department": item["department"],
                }
            )
            current_id += 1

        return result_data

    def top_users(self, faculties):
        """ получение общего рейтинга преподавателей  """
        result = []
        for f in faculties:
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    # print(u)
                    for c in u["current_category"]:
                        if c["result_point_fixed"] is not None:
                            if c["result_point_fixed"] > 0:
                                index += c["result_point_fixed"]
                        elif c["result_point"] > 0:
                            index += c["result_point"]
                    if index > 0:
                        result.append(
                            {
                                "name": u["name"],
                                "faculty": u["faculty"],
                                "department": u["department"],
                                "points": index,
                            }
                        )

        sorted_result = itertools.islice(
            reversed(sorted(result, key=lambda k: k["points"])), 20
        )

        return sorted_result

    def count_users_in_faculties(self, data):
        """ количество пользователей по факультетам """
        result = []
        sum_count = 0
        for f in data:
            count = 0
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    for c in u["current_category"]:
                        if c["result_point_fixed"] is not None:
                            if c["result_point_fixed"] > 0:
                                index += c["result_point_fixed"]
                        elif c["result_point"] > 0:
                            index += c["result_point"]
                    if index > 0:
                        count += 1
                        sum_count += 1
            result.append(
                {"name": f["name"], "count_users": count,}
            )
        result.append(
            {"name": "Все факультеты", "count_users": sum_count,}
        )
        return result

    # def name_category(self, data):
    #     """ Получение названия категории """
    #     for f in data:
    #         for d in f["departments"]:
    #             for u in d["users"]:
    #                 for c in u["current_category"]:
    #                     result = c["name"]
    #                     break
    #                 break
    #             break
    #         break

    #     print(result)
    #     return result

    def list_by_faculties(self, data, pk_category):
        """ составление списка всех пользователей """
        faculties = []
        for faculty in data:
            departments = []
            faculty_points = 0
            faculty_users = 0
            for department in faculty.departments.all():
                users = []
                department_points = 0
                department_users = 0
                for user_position in department.user_positions.all():
                    user_points = 0
                    department_users += 1
                    for qu in user_position.questionnaire_user.all():
                        # questionnaire = []
                        current_category = []
                        category = CategoryQuestionnaireUser.objects.filter(
                            questionnaire_user=qu,
                            category_questionnaire__parent_id=pk_category,
                        )

                        for point in category:
                            # print(point.questionnaire_user)
                            # print(point.result_point)
                            current_category.append(
                                {
                                    # "name": point.category_questionnaire.reference_category.name,
                                    "result_point": point.result_point,
                                    "result_point_fixed": point.result_point_fixed,
                                }
                            )

                        users.append(
                            {
                                "name": f"{user_position.user.last_name} {user_position.user.first_name} {user_position.user.patronymic}",
                                "current_category": current_category,
                                "faculty": user_position.department.faculty.name,
                                "department": user_position.department.name,
                            }
                        )

                    department_points += user_points

                faculty_points += department_points
                faculty_users += department_users
                departments.append(
                    {
                        "name": department.name,
                        "users": users,
                        "points": department_points,
                        "count_users": department_users,
                    }
                )
            faculties.append(
                {
                    "name": faculty.short_name,
                    "departments": departments,
                    "points": faculty_points,
                    "count_users": faculty_users,
                }
            )

        return faculties
