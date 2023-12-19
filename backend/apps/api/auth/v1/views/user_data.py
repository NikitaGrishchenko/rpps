import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.views import APIView


class UserData(APIView):
    """
    Информация об авторизированном пользователе
    """

    def get(self, request, format=None):
        user_model = get_user_model()
        user = user_model.objects.get(id=request.user.id)

        response_data = {
            "id": user.id,
            "username": user.username,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "patronymic": user.patronymic,
            "userImage": request.build_absolute_uri(user.user_image.url)
            if user.user_image
            else None,
            "email": user.email,
            "isAdmin": user.is_superuser,
            "isStaff": user.is_staff,
            "isManagerDepartment": user.is_manager_department,
            "managerDepartmentId": user.manager_department_id,
            "isManagerFaculty": user.is_manager_faculty,
            "managerFacultyId": user.manager_faculty_id,
            "isExpert": user.is_expert,
            "categoryExpertId": user.category_expert_id,
            "isSuperExpert": user.is_super_expert,
        }

        return JsonResponse(response_data)
