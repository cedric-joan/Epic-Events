from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class HasCustumerPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "SUP":
            return request.method in permissions.SAFE_METHODS
        return request.user.role == "SAL"