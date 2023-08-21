from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_permission(self, request: HttpRequest, view):
        return request.user and request.user.is_authenticated and request.user.is_staff or request.user.is_superuser
