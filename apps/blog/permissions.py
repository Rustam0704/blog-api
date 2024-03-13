from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        pass

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False


# post owerigina ozini post  detailini kora olsin


class IsStaffPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True
        else:
            return False
