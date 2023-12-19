# from apps.api.auth.models import UserPosition
# from apps.api.questioning.services import CreatingQuestionnaireUser
# from apps.api.reference.v1.serializers import (
#     CategorySerializer,
#     DescriptionCategorySerializer,
#     MainCategorySerializer,
# )
# from rest_framework import serializers
# from rest_framework_recursive.fields import RecursiveField

# from ...models import (
#     CategoryQuestionnaire,
#     MainCategoryQuestionnaire,
#     Questionnaire,
# )

# class CategoryQuestionnaireSerializer(serializers.ModelSerializer):
#     """ Категории анкеты """

#     reference_category = CategorySerializer()
#     childrens = RecursiveField(required=False, allow_null=True, many=True)

#     class Meta:
#         model = CategoryQuestionnaire
#         fields = "__all__"


# class MainCategoryQuestionnaireSerializer(serializers.ModelSerializer):
#     """ Главные категории анкеты """

#     category = CategoryQuestionnaireSerializer(read_only=True, many=True)
#     reference_category = MainCategorySerializer()

#     class Meta:
#         model = MainCategoryQuestionnaire
#         fields = "__all__"


# class QuestionnaireSerializer(serializers.ModelSerializer):
#     """ Анкета """

#     main_category = MainCategoryQuestionnaireSerializer(
#         read_only=True, many=True
#     )

#     class Meta:
#         model = Questionnaire
#         fields = "__all__"


# class CreatingQuestionnairesUsers(serializers.Serializer):
#     """ Массовое создание анкет и категорий для должностей пользователя """

#     user_positions = serializers.ListField(write_only=True)
#     questionnaires_users = serializers.ListField(write_only=True)

#     def create(self, validated_data):
#         user_positions = validated_data.pop("user_positions", None)
#         questionnaires_users = validated_data.pop("questionnaires_users", None)

#         if user_positions and questionnaires_users:
#             for user_position in user_positions:
#                 CreatingQuestionnaireUser.execute(
#                     {
#                         "user_position_id": user_position,
#                         "questionnaires": questionnaires_users,
#                     }
#                 )

#         return validated_data
