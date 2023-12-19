from datetime import datetime

from apps.api.auth.models import User, UserPosition
from apps.api.questioning.models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaire,
    Questionnaire,
    QuestionnaireUser,
)
from apps.api.questioning.services import get_result_questionnaire_user
from apps.api.reference.models import Department
from django.db.models import Q
from django.db.models.query import Prefetch
from django.utils.encoding import iri_to_uri
from django_weasyprint import WeasyTemplateView
from transliterate import translit

from ..services import XLSXView


class AllUsersXLSXPrint(XLSXView):
    """
    Файл кафедры xlsx
    """

    def get_file_name(self, **kwargs):
        date = datetime.now().strftime("%d_%m_%Y")
        extension = ".xlsx"
        return "all_users_" + date + extension

    def get_context_data(self, **kwargs):
        questionnaires_users = QuestionnaireUser.objects.filter(
            questionnaire_id=kwargs["pk_questionnaire"],
            user_position__department__isnull=False,
        )
        return {"questionnaires_users": questionnaires_users}

    def create_file(self, context, workbook, worksheet, **kwargs):
        bold = workbook.add_format({"bold": True})
        worksheet.write(0, 0, "Код", bold)
        worksheet.write(0, 1, "Фамилия", bold)
        worksheet.write(0, 2, "Имя", bold)
        worksheet.write(0, 3, "Отчество", bold)
        worksheet.write(0, 4, "Ставка", bold)
        worksheet.write(0, 5, "Код кафедры", bold)
        worksheet.write(0, 6, "Код факультета", bold)
        worksheet.write(0, 7, "Итоговый балл", bold)

        questionnaires_users = context["questionnaires_users"]

        for row_num, questionnaire_user in enumerate(questionnaires_users):

            #
            user = questionnaire_user.user_position.user
            worksheet.write(row_num + 1, 0, user.id)
            worksheet.write(row_num + 1, 1, user.last_name)
            worksheet.write(row_num + 1, 2, user.first_name)
            worksheet.write(row_num + 1, 3, user.patronymic)

            #
            rating = get_result_questionnaire_user(questionnaire_user)
            if questionnaire_user.user_position.rate is None:
                rate = ""
            else:
                rate = str(questionnaire_user.user_position.rate.value)
            worksheet.write(
                row_num + 1, 4, rate,
            )
            worksheet.write(
                row_num + 1,
                5,
                questionnaire_user.user_position.department.name,
            )
            worksheet.write(
                row_num + 1,
                6,
                questionnaire_user.user_position.department.faculty.name,
            )
            worksheet.write(row_num + 1, 7, rating)


class DepartmentXLSXPrint(XLSXView):
    """
    Файл кафедры xlsx
    """

    def get_file_name(self, **kwargs):
        # date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        date = datetime.now().strftime("%d_%m_%Y")
        department = (
            Department.objects.all()
            .select_related("faculty")
            .get(pk=kwargs["pk_department"],)
        )
        department_name = department.short_name
        faculty_name = department.faculty.short_name
        file_name = f"{faculty_name} {department_name} "
        extension = ".xlsx"
        return (
            translit(file_name.replace(" ", "_"), "ru", reversed=True)
            + date
            + extension
        )

    def get_context_data(self, **kwargs):
        users = (
            User.common_users.all()
            .prefetch_related(
                Prefetch(
                    "user_positions",
                    queryset=UserPosition.objects.filter(
                        questionnaire_user__questionnaire_id=kwargs[
                            "pk_questionnaire"
                        ]
                    ).select_related("department", "rate", "position"),
                )
            )
            .filter(user_positions__department_id=kwargs["pk_department"],)
        )
        return {"users": users}

    def get_questionnaire_categories_user(self, questionnaire_user, count_categories_questionnaire):

        result = []
        for number_category in range(1, count_categories_questionnaire+1):
            categories = CategoryQuestionnaireUser.objects.filter(
                Q(questionnaire_user=questionnaire_user),
                Q(Q(category_questionnaire__number=number_category) & Q(category_questionnaire__main_category__isnull=False)) |
                Q(Q(category_questionnaire__parent__number=number_category) & Q(category_questionnaire__parent__main_category__isnull=False)) |
                Q(Q(category_questionnaire__parent__parent__number=number_category) & Q(category_questionnaire__parent__parent__main_category__isnull=False))
                )


            sum_category = 0

            for category in categories:
                pass
                if category.result_point_fixed is not None:
                    sum_category += category.result_point_fixed
                else:
                    sum_category += category.result_point

            result.append(
                    {"number": number_category, "point": sum_category}
                )

        return result


    def create_file(self, context, workbook, worksheet, **kwargs):
        bold = workbook.add_format({"bold": True})
        worksheet.write(0, 0, "Фамилия", bold)
        worksheet.write(0, 1, "Имя", bold)
        worksheet.write(0, 2, "Отчество", bold)
        worksheet.write(0, 3, "Ставка", bold)
        worksheet.write(0, 4, "Код кафедры", bold)
        worksheet.write(0, 5, "Код факультета", bold)
        worksheet.write(0, 6, "Итоговый балл", bold)


        count_categories_questionnaire = CategoryQuestionnaire.objects.filter(main_category__questionnaire__pk=kwargs["pk_questionnaire"]).order_by('-number').first().number

        for col in range(1, count_categories_questionnaire+1):
            worksheet.write(0, col+6, col, bold)

        users = context["users"]

        for row_num, user in enumerate(users):
            worksheet.write(row_num + 1, 0, user.last_name)
            worksheet.write(row_num + 1, 1, user.first_name)
            worksheet.write(row_num + 1, 2, user.patronymic)
            try:
                position = user.user_positions.all().get(
                    user_id=user.id, department_id=kwargs["pk_department"]
                )
                if position:
                    rating = get_result_questionnaire_user(
                        position.questionnaire_user.get(
                            questionnaire_id=kwargs["pk_questionnaire"]
                        )
                    )


                    if position.rate is None:
                        rate = ""
                    else:
                        rate = str(position.rate.value)
                    worksheet.write(
                        row_num + 1, 3, rate,
                    )
                    worksheet.write(
                        row_num + 1,
                        4,
                        user.user_positions.all()
                        .get(user_id=user.id)
                        .department.rsue_id,
                    )
                    worksheet.write(
                        row_num + 1,
                        5,
                        user.user_positions.all()
                        .get(user_id=user.id)
                        .department.faculty.rsue_id,
                    )
                    worksheet.write(row_num + 1, 6, rating)

                    questionnaire_categories_user = list(reversed(self.get_questionnaire_categories_user(position.questionnaire_user.get(questionnaire_id=kwargs["pk_questionnaire"]), count_categories_questionnaire)))

                    for item in questionnaire_categories_user:
                        worksheet.write(row_num + 1, item["number"]+6, str(item["point"]))


            except:
                worksheet.write(row_num + 1, 4, "Ошибка")






class QuestionnairePrint(WeasyTemplateView):
    """
    Анкета пользователя
    """

    template_name = "documents/questionary.html"

    def get_pdf_filename(self):
        pk_questionnaire_user = self.kwargs["pk_questionnaire_user"]
        user = self.get_user(pk_questionnaire_user)
        questionnaire_user = self.get_questionnaire(pk_questionnaire_user)
        faculty = questionnaire_user.user_position.department.faculty
        year = questionnaire_user.questionnaire.name[7:11]
        filename = (
            f"РППС{year}_{faculty}_{user.last_name} {user.first_name}.pdf"
        )
        print(questionnaire_user.questionnaire.name)
        return iri_to_uri(filename)

    def get_points(self, category):
        """
        """
        if (
            category.category_questionnaire_user.first().result_point_fixed
            is None
        ):
            return category.category_questionnaire_user.first().result_point
        else:
            return (
                category.category_questionnaire_user.first().result_point_fixed
            )

    def get_user(self, pk_questionnaire_user):
        """
        Возвращает информацию о владельце анкеты
        """

        return User.objects.get(
            user_positions__questionnaire_user=pk_questionnaire_user
        )

    def get_questionnaire(self, pk_questionnaire_user):
        """
        Возвращает анкету пользователя
        """
        return (
            QuestionnaireUser.objects.filter(pk=pk_questionnaire_user)
            .prefetch_related(
                Prefetch(
                    "questionnaire",
                    queryset=Questionnaire.objects.all().prefetch_related(
                        Prefetch(
                            "main_category",
                            queryset=MainCategoryQuestionnaire.objects.all()
                            .select_related("reference_category")
                            .prefetch_related(
                                Prefetch(
                                    "category",
                                    queryset=CategoryQuestionnaire.objects.select_related(
                                        "periodicity",
                                        "reference_category",
                                        "reference_category__description",
                                    ).prefetch_related(
                                        Prefetch(
                                            "childrens",
                                            queryset=CategoryQuestionnaire.objects.select_related(
                                                "periodicity",
                                                "reference_category",
                                                "reference_category__description",
                                            ).prefetch_related(
                                                Prefetch(
                                                    "childrens",
                                                    queryset=CategoryQuestionnaire.objects.select_related(
                                                        "periodicity",
                                                        "reference_category",
                                                        "reference_category__description",
                                                    ).prefetch_related(
                                                        Prefetch(
                                                            "childrens",
                                                            queryset=CategoryQuestionnaire.objects.select_related(
                                                                "periodicity",
                                                                "reference_category",
                                                                "reference_category__description",
                                                            ),
                                                        ),
                                                        Prefetch(
                                                            "category_questionnaire_user",
                                                            queryset=CategoryQuestionnaireUser.objects.filter(
                                                                questionnaire_user=pk_questionnaire_user
                                                            ).prefetch_related(
                                                                "files"
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Prefetch(
                                                    "category_questionnaire_user",
                                                    queryset=CategoryQuestionnaireUser.objects.filter(
                                                        questionnaire_user=pk_questionnaire_user
                                                    ).prefetch_related(
                                                        "files"
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Prefetch(
                                            "category_questionnaire_user",
                                            queryset=CategoryQuestionnaireUser.objects.filter(
                                                questionnaire_user=pk_questionnaire_user
                                            ).prefetch_related(
                                                "files"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                )
            )
            .first()
        )

    def get_rating(self, data):
        """
        Возвращает рейтинг
        """
        result = []
        count_category = 0
        count_user_category = 0
        summ_result_rating = 0

        for main_category in data.questionnaire.main_category.all():
            shortName = main_category.reference_category.short_name
            result_rating = 0
            if (
                main_category.main_category_questionnaire_user.get(
                    questionnaire_user=data
                ).result_point_fixed
                is not None
            ):
                result_rating += main_category.main_category_questionnaire_user.get(
                    questionnaire_user=data
                ).result_point_fixed
                summ_result_rating = summ_result_rating + result_rating

                result.append(
                    {
                        "shortName": shortName,
                        "result": str(result_rating).split(".")[0]
                        + "."
                        + str(result_rating).split(".")[1][:2],
                    }
                )
                continue
            for category_1 in main_category.category.all():
                if category_1.type_category is not None:
                    count_category = count_category + 1
                if len(category_1.category_questionnaire_user.all()) != 0:
                    count_user_category = count_user_category + 1
                    result_rating = result_rating + self.get_points(category_1)

                for category_2 in category_1.childrens.all():
                    if category_2.type_category is not None:
                        count_category = count_category + 1
                    if len(category_2.category_questionnaire_user.all()) != 0:
                        count_user_category = count_user_category + 1

                        result_rating = result_rating + self.get_points(
                            category_2
                        )

                    for category_3 in category_2.childrens.all():
                        if category_3.type_category is not None:
                            count_category = count_category + 1
                        if (
                            len(category_3.category_questionnaire_user.all())
                            != 0
                        ):
                            count_user_category = count_user_category + 1

                            result_rating = result_rating + self.get_points(
                                category_3
                            )

            summ_result_rating = summ_result_rating + result_rating
            result.append(
                {
                    "shortName": shortName,
                    "result": str(result_rating).split(".")[0]
                    + "."
                    + str(result_rating).split(".")[1][:2],
                }
            )

        result.append(
            {"shortName": "Общий балл", "result": round(summ_result_rating, 2)}
        )
        # result.append(
        #     {
        #         "shortName": "Процент заполненности",
        #         "result": str(
        #             round(count_user_category * 100 / count_category, 2)
        #         )
        #         + "%",
        #     }
        # )

        return result

    def get_context_data(self, **kwargs):
        """
        Контекст PDF документа
        """
        context = super().get_context_data(**kwargs)
        pk_questionnaire_user = kwargs["pk_questionnaire_user"]
        user = self.get_user(pk_questionnaire_user)
        questionnaire_user = self.get_questionnaire(pk_questionnaire_user)

        context["user"] = user
        context["questionnaire_user"] = questionnaire_user
        context["ratings"] = self.get_rating(questionnaire_user)
        context["date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        context["year"] = questionnaire_user.questionnaire.name[7:11]

        return context
