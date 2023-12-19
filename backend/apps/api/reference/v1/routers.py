from django.conf.urls import include
from django.urls import path

from .views import (  # BaseChoiceView,
    BannerListAPIView,
    DepartmentAPIList,
    DepartmentAPIRetrieve,
    FacultyAPIList,
    FacultyAPIRetrieve,
    PositionAPIList,
    PrizePlaceAPIList,
    RateAPIList,
    StatusQuestionnaireList,
    TypeCategoryList,
    TypeFileList,
)

app_name = "reference"

urlpatterns = [
    path("banners/", BannerListAPIView.as_view()),
    path("prize-places/", PrizePlaceAPIList.as_view()),
    path("departments/", DepartmentAPIList.as_view()),
    path("positions/", PositionAPIList.as_view()),
    path("rates/", RateAPIList.as_view()),
    path("faculty/", FacultyAPIList.as_view()),
    path("faculty/<int:pk_faculty>/", FacultyAPIRetrieve.as_view()),
    path("department/<int:pk_department>/", DepartmentAPIRetrieve.as_view(),),
    path(
        "enums/",
        include(
            [
                path("type-category/", TypeCategoryList.as_view()),
                path(
                    "status-questionnaire/", StatusQuestionnaireList.as_view(),
                ),
                path("type-file/", TypeFileList.as_view()),
            ]
        ),
    ),
]
