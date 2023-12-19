from rest_framework.permissions import BasePermission


class RoleManagerDepartment(BasePermission):
    """ Пользователь яаляется - заведующим кафедры """

    def has_permission(self, request, view):
        return request.user.role_manager_department


class RoleManagerFaculty(BasePermission):
    """ Пользователь яаляется - деканом """

    def has_permission(self, request, view):
        return request.user.role_manager_faculty


class RoleExpert(BasePermission):
    """ Пользователь яаляется - экспертом """

    def has_permission(self, request, view):
        return request.user.role_expert


class RoleSuperExpert(BasePermission):
    """ Пользователь яаляется - супер экспертом """

    def has_permission(self, request, view):
        return request.user.role_super_expert
