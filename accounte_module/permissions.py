from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS


class PermissionEditUserProfile(BasePermission):

    def has_permission(self, request: HttpRequest, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id