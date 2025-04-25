"""Модуль для проверки полномочий действий пользователя над объектами."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверяет полномочие на изменение или удаления поста только его автором.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
