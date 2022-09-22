from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) or request.method == 'GET'