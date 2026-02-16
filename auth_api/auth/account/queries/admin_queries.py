from django.contrib.auth import get_user_model
from auth_api.auth.account.models import (Role)
from rest_framework.response import Response
from rest_framework import status 
from django.db.models import Q
# Create Your Queries : 

def get_user(id) : 
    try :
        user = get_user_model().objects.get(id = id)
        print(type(user))
        return user
    except get_user_model().DoesNotExist :
        return Response({"errors" : "USER DOESE NOT EXIST!"} , status=status.HTTP_404_NOT_FOUND)
    

def get_user_hospitals_id(user , is_active = True) : 

    query = user.userHospitals.filter(is_active = is_active).values_list("hospital_id" , flat = True)

    return query

def get_user_roles_id(user , is_active = True) :

    query = user.userHospitals.filter(is_active = is_active ).values_list("role_id" , flat = True)

    return query

def get_user_roles_name(user_roles_id) :

    query = Role.objects.filter(id__in = user_roles_id)

    return query
def user_role_in_hospital(user,hospital_id, is_active = True) : 
    query = user.userHospitals.filter(is_active = is_active , hospital_id = hospital_id).values_list("role__name",flat = True)
    return query


SUPER_ADMIN_ALLOWED_LIST = ["Admin","Doctor", "Nurse",]
ADMIN_ALLOWED_LIST = ["Doctor", "Nurse",]
DOCTOR_ALLOWED_LIST = ["Nurse",]
ALLOWED_LIST = []

def get_user_list_by_hospital_id(user,hospital_id,is_active = True,) :
    """
    Docstring for get_user_list_by_hospital_id
    
    :param user: get request.user
    :param hospital_id: get hospital_id(for ex :from url)
    :param is_active: it say the roles that there are still active 
    """
    
    # user_hospitals_id   = get_user_hospitals_id(user ,is_active)
    # user_roles_names    = get_user_roles_name(user_roles_id)
    # user_roles_id       = get_user_roles_id(user , is_active)

    # TODO : I Shoul Daynamic and check user role

    user_role           = user_role_in_hospital(user , hospital_id , is_active)
    
    if "SuperAdmin" in user_role :
        ALLOWED_LIST = SUPER_ADMIN_ALLOWED_LIST
    if "Admin" in user_role :
        ALLOWED_LIST = ADMIN_ALLOWED_LIST
    if "Doctor" in user_role :
        ALLOWED_LIST = DOCTOR_ALLOWED_LIST

    query = get_user_model().objects.filter(
        Q(userHospitals__hospital_id = hospital_id) 
        &
        Q(userHospitals__role__name__in = ALLOWED_LIST)
    ).distinct()

    return query
    