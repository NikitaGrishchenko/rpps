from apps.api.auth.models import UserPosition
from apps.api.reference.models import Department, Faculty
from django.core.management.base import BaseCommand
from django.db.models.query import Prefetch
from py_linq import Enumerable
from tqdm import tqdm

from ...models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaireUser,
    QuestionnaireUser,
)


class Rating:
    """ Rating """

    def _get_data_faculty(self):
        """
        Исходные данные
        """
        prefetch_main_category_questionnaire_user = Prefetch(
            "main_category_questionnaire_user",
            queryset=MainCategoryQuestionnaireUser.objects.all(),
        )
        prefetch_questionnaire_user = Prefetch(
            "questionnaire_user",
            queryset=QuestionnaireUser.objects.all().prefetch_related(
                prefetch_main_category_questionnaire_user
            ),
        )
        prefetch_user_positions = Prefetch(
            "user_positions",
            queryset=UserPosition.objects.all().prefetch_related(
                prefetch_questionnaire_user
            ),
        )
        prefetch_departments = Prefetch(
            "departments",
            queryset=Department.objects.all().prefetch_related(
                prefetch_user_positions
            ),
        )
        data = Faculty.objects.all().prefetch_related(prefetch_departments)
        return data

    def get_actual_points(self, category):
        """
        актуальный балл
        """
        if category.result_point_fixed is None:
            return category.result_point
        else:
            return category.result_point_fixed

    def __init__(self):
        self._data = []
        self._faculties_queryset = self._get_data_faculty()

        for f in self._faculties_queryset:
            departments = []
            faculty_points = 0
            faculty_users = 0
            for d in f.departments.all():
                users = []
                department_points = 0
                department_users = 0
                for up in d.user_positions.all():
                    user_points = 0
                    department_users += 1
                    for qu in up.questionnaire_user.all():
                        questionnaire = []
                        h_index_list = []
                        rinc_list = []
                        h_index = CategoryQuestionnaireUser.objects.filter(
                            questionnaire_user=qu,
                            category_questionnaire__parent_id=70,
                        )
                        rinc = CategoryQuestionnaireUser.objects.filter(
                            questionnaire_user=qu,
                            category_questionnaire__parent_id=74,
                        )
                        for point in rinc:
                            rinc_list.append(
                                {
                                    "name": point.category_questionnaire.reference_category.name,
                                    "result_point": point.result_point,
                                    "result_point_fixed": point.result_point_fixed,
                                }
                            )
                        for point in h_index:
                            h_index_list.append(
                                {
                                    "name": point.category_questionnaire.reference_category.name,
                                    "result_point": point.result_point,
                                    "result_point_fixed": point.result_point_fixed,
                                }
                            )
                        for mc in qu.main_category_questionnaire_user.all():
                            mc_points = self.get_actual_points(mc)
                            user_points += mc_points
                            questionnaire.append(
                                {
                                    "name": mc.main_category_questionnaire.reference_category.name,
                                    "points": mc_points,
                                }
                            )

                    department_points += user_points
                    users.append(
                        {
                            "name": f"{up.user.last_name} {up.user.first_name} {up.user.patronymic}",
                            "questionnaire": questionnaire,
                            "h_index": h_index_list,
                            "rinc": rinc_list,
                            "points": user_points,
                            "faculty": up.department.faculty.name,
                            "department": up.department.name,
                        }
                    )
                faculty_points += department_points
                faculty_users += department_users
                departments.append(
                    {
                        "name": d.name,
                        "users": users,
                        "points": department_points,
                        "count_users": department_users,
                    }
                )
            self._data.append(
                {
                    "name": f.short_name,
                    "departments": departments,
                    "points": faculty_points,
                    "count_users": faculty_users,
                }
            )

    @property
    def count_users(self):
        """
        Кол-во всех пользователей
        """
        count_users = 0
        for f in self._data:
            count_users += f["count_users"]
        return count_users

    @property
    def score(self):
        """
        Общий балл
        """
        score = 0
        for f in self._data:
            score += f["points"]
        return score

    @property
    def average_score(self):
        """
        Средний балл
        """
        return self.score / self.count_users

    @property
    def rating_faculty(self):
        """
        Рейтинг по факультету
        """
        rating_faculty = []
        for f in self._data:
            rating_faculty.append(
                {"name": f["name"], "value": f["points"] / f["count_users"]}
            )
        return rating_faculty

    @property
    def data(self):
        """
        Исходные данные
        """
        return self._data

    @property
    def get_points_direction(self):
        result = {}
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    for q in u["questionnaire"]:
                        if q["name"] in result.keys():
                            result[q["name"]] += q["points"]
                        else:
                            result[q["name"]] = q["points"]
        print(result)
        return result

    def get_average(self):
        """
        Средний балл
        ('Все разделы' + напрвления)
        """
        result = []
        for key, value in self.get_points_direction.items():
            result.append(
                {"name": key, "points": value / self.count_users,}
            )
        result.append({"name": "Все разделы", "points": self.average_score})
        return result

    def get_average_higher(self):
        """
        Количество преподавателей,
        набравших баллы выше среднего
        """
        result = []
        average = self.get_average()
        for a in average:
            result.append(
                {"name": a["name"], "count_users": 0, "points": a["points"]}
            )
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    for q in u["questionnaire"]:
                        for a in result:
                            if q["name"] == a["name"]:
                                if q["points"] > a["points"]:
                                    a["count_users"] += 1
                            if a["name"] == "Все разделы":
                                if u["points"] > a["points"]:
                                    a["count_users"] += 1 / 4

        # next(r for r in result if r["name"] == "Pam")
        return result

    def get_average_lower(self):
        """
        Количество преподавателей,
        набравших баллы ниже среднего
        """
        result = []
        average = self.get_average()
        for a in average:
            result.append(
                {"name": a["name"], "count_users": 0, "points": a["points"]}
            )
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    for q in u["questionnaire"]:
                        for a in result:
                            if q["name"] == a["name"]:
                                if q["points"] < a["points"]:
                                    a["count_users"] += 1
                            if a["name"] == "Все разделы":
                                if u["points"] < a["points"]:
                                    a["count_users"] += 1 / 4
        return result

    def average_score_faculties(self):
        result = []

        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    for q in u["questionnaire"]:
                        result.append(
                            {"name": q["name"], "faculties": [],}
                        )
                    break
                break
            break
        for r in result:
            for f in self._data:
                points = 0
                count_users = 0
                for d in f["departments"]:
                    for u in d["users"]:
                        count_users += 1
                        for q in u["questionnaire"]:
                            if r["name"] == q["name"]:
                                points += q["points"]
                r["faculties"].append(
                    {"name": f["name"], "points": points / count_users}
                )

        return result

    def get_rating_departments(self):
        result = []
        for f in self._data:
            for d in f["departments"]:
                result.append(
                    {
                        "name": d["name"],
                        "points": d["points"] / d["count_users"],
                    }
                )
        sorted_result = sorted(result, key=lambda k: k["points"])
        return reversed(sorted_result)

    def get_index_object(self):
        result = []
        for f in self._data:
            count = 0
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    for c in u["h_index"]:
                        if c["result_point_fixed"] is not None:
                            if c["result_point_fixed"] > 0:
                                index += c["result_point_fixed"]
                        elif c["result_point"] > 0:
                            index += c["result_point"]
                    if index > 0:
                        count += 1
            result.append(
                {"name": f["name"], "count_useres": count,}
            )
        return result

    def get_rinc_object(self):
        result = []
        for f in self._data:
            count = 0
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    for c in u["rinc"]:
                        if c["result_point_fixed"] is not None:
                            if c["result_point_fixed"] > 0:
                                index += c["result_point_fixed"]
                        elif c["result_point"] > 0:
                            index += c["result_point"]
                    if index > 0:
                        count += 1
            result.append(
                {"name": f["name"], "count_useres": count,}
            )
        return result

    def get_users_h_index(self):
        result = []
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    for c in u["h_index"]:
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
        sorted_result = sorted(result, key=lambda k: k["points"])
        return sorted_result

    def get_users_rinc(self):
        result = []
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    index = 0
                    for c in u["rinc"]:
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

        sorted_result = sorted(result, key=lambda k: k["points"])
        return sorted_result

    def top_nir(self):
        result = []
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    for q in u["questionnaire"]:
                        if (
                            q["name"]
                            == "Научно-исследовательская и инновационная деятельность"
                        ):
                            result.append(
                                {
                                    "name": u["name"],
                                    "faculty": u["faculty"],
                                    "department": u["department"],
                                    "points": q["points"],
                                }
                            )
        sorted_result = sorted(result, key=lambda k: k["points"])
        return sorted_result

    def display(self):
        for f in self._data:
            for d in f["departments"]:
                for u in d["users"]:
                    if len(u["category"]) > 3:
                        print(u["name"])
                        print(u["category"])


class Command(BaseCommand):
    """ Класс команды """

    help = "Итоговый отчет"

    def handle(self, *args, **options):
        """
        Обработчик команды
        """
        rating = Rating()

        # print("     Слайд 1")
        # print(f"Количество преподавателей: {rating.count_users}")

        # print("     Слайд 2")
        # print(f"Средний балл: {rating.average_score}")

        # print("     Слайд 3")
        # print("Средний балл:")
        # for average in rating.get_average():
        #     print(f"{average['name']} {average['points']}")
        # print("Количество преподавателей, набравших баллы ниже среднего:")
        # for lower in rating.get_average_lower():
        #     print(f"{lower['name']} {lower['count_users']}")
        # print("Количество преподавателей, набравших баллы выше среднего:")
        # for higher in rating.get_average_higher():
        #     print(f"{higher['name']} {higher['count_users']}")

        # print("     Слайд 4")
        # for f in rating.rating_faculty:
        #     print(f"{f['name']} {f['value']}")

        # print("     Слайд 5")
        # for f in rating.rating_faculty:
        #     print(f"{f['name']} {f['value']}")

        # print("     Слайд 6")
        # print("Преподаватели, набравшие наибольшее общее количество баллов")

        # print("     Слайд 7-9")
        # for d in rating.average_score_faculties():
        #     print(f"    {d['name']}")
        #     for f in d["faculties"]:
        #         print(f"        {f['name']} - {f['points']}")

        # print("     Слайд 13")
        # for d in rating.get_rating_departments():
        #     print(f"{d['name']}; {d['points']}")

        # print("Количество преподавателей, имеющих индекс Хирша")
        # all_index = 0
        # for r in rating.get_index_object():
        #     all_index += r["count_useres"]
        #     print(f"{r['name']}; {r['count_useres']}")
        # print(f"Всего; {all_index}")

        # print("Количество преподавателей, цитируемых в РИНЦ")
        # all_rinc = 0
        # for r in rating.get_rinc_object():
        #     all_rinc += r["count_useres"]
        #     print(f"{r['name']}; {r['count_useres']}")
        # print(f"Всего; {all_rinc}")

        print("Хирша")
        h_index_users = rating.get_users_h_index()
        for r in h_index_users[-20:]:
            print(
                f"{r['name']}; {r['points']}; {r['faculty']}; {r['department']}"
            )
        print("ринц")
        rinc_users = rating.get_users_rinc()
        for r in rinc_users[-20:]:
            print(
                f"{r['name']}; {r['points']}; {r['faculty']}; {r['department']}"
            )
        # print()
        # print("Топ НИР")
        # top_nir = rating.top_nir()
        # for r in top_nir[-50:]:
        #     print(
        #         f"{r['name']}; {r['points']}; {r['faculty']}; {r['department']}"
        #     )
