def recursive_get_main_category(category_questionnaire):
    """
    Возвращает родительскую главную категорию
    """
    if category_questionnaire.main_category is None:
        return recursive_get_main_category(category_questionnaire.parent)
    return category_questionnaire.main_category
