from rest_framework.permissions import BasePermission

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
            return request.user.is_active
        