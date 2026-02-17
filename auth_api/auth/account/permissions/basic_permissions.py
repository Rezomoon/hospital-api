from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from auth_api.auth.account.queries.admin_queries import ( get_user_hospitals_id , )
# Create Your Permissions : 
class NotNurse(permissions.BasePermission) : 
    def has_permission(self, request, view):

        return bool(request.user and not "Nurse" in request.user.userHospitals.filter(is_active = True).values_list("role__name",flat = True))

class SameHospital(permissions.BasePermission) : 
    def has_object_permission(self, request, view, obj):

        hospitals_id = get_user_hospitals_id(user=request.user)

        obj_query = obj.userHospitals.filter(is_active = True).values_list("hospital_id" , flat  = True)

        for q in obj_query :

                return bool(q in hospitals_id )
            
        return False

class IsAdminOrSuperUser(permissions.BasePermission) :
     """

     Docstring for IsAdminOrSuperUser : 
        It Check Permissions With Flags Like
            is_admin , is_staff, is_superuser .

     """
     def has_permission(self, request, view):
          
          user = request.user # It mean The User Has Login !

          return bool(user and user.is_staff or user.is_superuser or user.is_admin )