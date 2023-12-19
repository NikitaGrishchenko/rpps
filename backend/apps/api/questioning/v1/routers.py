from django.urls import include, path

from .views import (
    AllYearsOfUserDocumentsList,
    CategoryQuestionnaireUserAPIListCreate,
    CategoryQuestionnaireUserAPIUdpate,
    CategoryQuestionnaireUserAttachFileAPIView,
    CategoryQuestionnaireUserRetriveAPIView,
    CategoryQuestionnaireUserUploadFileAPIView,
    ConfirmEffectiveContract,
    DocumentsOfOneYearList,
    FileCategoryQuestionnaireUserAPIDelete,
    FileCategoryQuestionnaireUserAPIUpdate,
    FileCategoryQuestionnaireUserRetrieveAPIView,
    MainCategoryQuestionnaireUserAPIUpdate,
    QuestionnaireAllAPIList,
    QuestionnaireDepartmentAPIList,
    QuestionnairesUsersCreate,
    QuestionnaireUserAPIList,
    QuestionnaireUserAPIRetrive,
    QuestionnaireUserCheckExpertAPIRetrive,
    StatisticsByCategoryApi,
    StatisticsQuestionnaire,
    UserFileAPIListCreate,
    UserFileAPIRetrieveUpdateDestroy,
)

app_name = "questioning"

# url /questionnaire/

urlpatterns = [
    # Получения списка всех имеющихся анкет для пользователя
    path("list/", QuestionnaireUserAPIList.as_view()),
    path(
        "list-department/<int:pk_department>/",
        QuestionnaireDepartmentAPIList.as_view(),
    ),
    path("all-list/", QuestionnaireAllAPIList.as_view()),
    path(
        "detail/<int:pk_questionnaire>/",
        QuestionnaireUserAPIRetrive.as_view(),
    ),
    path(
        "expert/detail/<int:pk_questionnaire>/",
        QuestionnaireUserCheckExpertAPIRetrive.as_view(),
    ),
    path(
        "expert/change-category/<int:pk>/",
        CategoryQuestionnaireUserAPIUdpate.as_view(),
    ),
    path(
        "category-user/<int:pk_category>/",
        CategoryQuestionnaireUserRetriveAPIView.as_view(),
    ),
    path(
        "category-user/upload-file/<int:pk_category>/",
        CategoryQuestionnaireUserUploadFileAPIView.as_view(),
    ),
    path(
        "category-user/attach-file/<int:pk_category>/",
        CategoryQuestionnaireUserAttachFileAPIView.as_view(),
    ),
    path(
        "category-user/update-file/<int:pk_file>/",
        FileCategoryQuestionnaireUserAPIUpdate.as_view(),
    ),
    path(
        "category-user/delete-file/<int:pk_file>/",
        FileCategoryQuestionnaireUserAPIDelete.as_view(),
    ),
    path(
        "category-user/retrieve-file/<int:pk_file>/",
        FileCategoryQuestionnaireUserRetrieveAPIView.as_view(),
    ),
    path(
        "confirm-effective-contract/<int:pk>/",
        ConfirmEffectiveContract.as_view(),
    ),
    path(
        "main-category-user/<int:pk>/",
        MainCategoryQuestionnaireUserAPIUpdate.as_view(),
    ),
    path("files/", UserFileAPIListCreate.as_view()),
    path("files/<int:pk>/", UserFileAPIRetrieveUpdateDestroy.as_view()),
    path("files/years/", AllYearsOfUserDocumentsList.as_view()),
    path("files/for-year/<int:year>/", DocumentsOfOneYearList.as_view()),
    path("creation-for-all/", QuestionnairesUsersCreate.as_view()),
    path("statistics/<int:pk>/", StatisticsQuestionnaire.as_view()),
    path(
        "statistics-by-category/<int:pk_category>/",
        StatisticsByCategoryApi.as_view(),
    ),
]
