from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверям что только автор имеет доступ к POST, PUT и т.д.
    Остальные имеют доступ только к GET."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
