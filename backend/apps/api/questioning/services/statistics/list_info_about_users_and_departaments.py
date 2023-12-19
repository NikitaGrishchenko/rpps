def actual_points_category(category):
    """ актуальный балл для категорий """

    if category.result_point_fixed is None:
        return category.result_point
    else:
        return category.result_point_fixed


def list_info_about_users_and_departaments(queryset):
    """ получение всей информации о пользователях и кафедрах, сохранения информации в одноименные массивы"""

    faculties = []

    for faculty in queryset:

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
                    questionnaire = []
                    for mc in qu.main_category_questionnaire_user.all():
                        mc_points = actual_points_category(mc)
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
                        "name": f"{user_position.user.last_name} {user_position.user.first_name} {user_position.user.patronymic}",
                        "questionnaire": questionnaire,
                        # "h_index": h_index_list,
                        # "rinc": rinc_list,
                        "points": user_points,
                        "faculty": user_position.department.faculty.name,
                        "department": user_position.department.name,
                    }
                )
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
