def get_points_category_questionnaire(
    category_questionnaire, questionnaire_user
):
    """
    Возвращает балл по категории анкеты и анкете пользователя
    """
    category = category_questionnaire.category_questionnaire_user.filter(
        questionnaire_user=questionnaire_user
    ).first()
    if category:
        # return category.get_actual_points()
        if category.result_point_fixed is None:
            return category.result_point
        return category.result_point_fixed
    return 0
