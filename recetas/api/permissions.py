from rest_framework.permissions import BasePermission

#class IsAdminReadOnly(BasePermission):
 #   def has_permission(self, request, view):
  #      if request.method in [ 'GET', 'POST', 'DELETE', 'PUT', 'PATCH']:
        # if request.method in [ 'GET', 'POST']:
            # return request.user.is_active #Permiso de esta logeado
   #         return True
    #    else:
     #       return request.user.is_staff
        

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in [ 'GET']:
            # Otorgar permiso si el usuario está autenticado
            return True
        elif request.method in ['POST', 'DELETE', 'PUT', 'PATCH']:
            return request.user.is_authenticated
        else:
            return request.user.is_staff
