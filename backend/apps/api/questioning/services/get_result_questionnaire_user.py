def get_result_questionnaire_user(questionnaire_user):
    """
    Возвращает балл по анкете пользователя
    """
    summ = 0
    for (
        main_category
    ) in questionnaire_user.main_category_questionnaire_user.all():
        if main_category.result_point_fixed is not None:
            summ += main_category.result_point_fixed
        else:
            summ += main_category.result_point
    return summ
