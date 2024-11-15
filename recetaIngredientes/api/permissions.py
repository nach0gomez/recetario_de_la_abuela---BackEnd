from rest_framework.permissions import BasePermission

#class IsAdminReadOnly(BasePermission):
 #   def has_permission(self, request, view):
        # return request.user.is_active
  #      return True
    
class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in [ 'GET', 'POST', 'DELETE', 'PUT', 'PATCH']:
            # Otorgar permiso si el usuario está autenticado
            return request.user.is_authenticated
        else:
            return request.user.is_staff
        