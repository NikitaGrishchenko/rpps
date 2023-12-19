from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.api.questioning.services import (
    recursive_get_main_category,
    get_points_category_questionnaire,
)
from .models import CategoryQuestionnaireUser, MainCategoryQuestionnaireUser


@receiver(post_save, sender=CategoryQuestionnaireUser)
def post_save_category_user(
    sender, instance: CategoryQuestionnaireUser, created: bool, **_kwargs
):
    """ Сигнал после сохранения категории пользователя """
    questionnaire_user = instance.questionnaire_user
    main_category = recursive_get_main_category(
        instance.category_questionnaire
    )
    result = 0
    for category_1 in main_category.category.all():
        if category_1.type_category is not None:
            result += get_points_category_questionnaire(
                category_1, questionnaire_user
            )
        for category_2 in category_1.childrens.all():
            if category_2.type_category is not None:
                result += get_points_category_questionnaire(
                    category_2, questionnaire_user
                )
            for category_3 in category_2.childrens.all():
                if category_3.type_category is not None:
                    result += get_points_category_questionnaire(
                        category_3, questionnaire_user
                    )

    main_category_questionnaire_user = MainCategoryQuestionnaireUser.objects.filter(
        main_category_questionnaire=main_category,
        questionnaire_user=questionnaire_user,
    ).first()
    main_category_questionnaire_user.result_point = result
    main_category_questionnaire_user.save()
