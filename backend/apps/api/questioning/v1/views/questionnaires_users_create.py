from apps.api.questioning.v1.serializers import CreatingQuestionnairesUsers
from rest_framework import generics


class QuestionnairesUsersCreate(generics.CreateAPIView):

    serializer_class = CreatingQuestionnairesUsers
