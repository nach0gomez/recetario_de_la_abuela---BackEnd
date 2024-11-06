from rest_framework.permissions import BasePermission

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in [ 'GET', 'POST', 'DELETE']:
            # return request.user.is_active #Permiso de esta logeado
            return True
        else:
            return request.user.is_staff
        
        
        
    
    
    