from django.contrib.auth import get_user_model
from auth_api.auth.account.models import (Role)
from rest_framework.response import Response
from rest_framework import status 
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
    

SUPER_ADMIN_ALLOWED_LIST = ["Admin","Doctor", "Nurse",]
ADMIN_ALLOWED_LIST = ["Doctor", "Nurse",]
DOCTOR_ALLOWED_LIST = ["Nurse",]
ALLOWED_LIST = []

def get_user_list(user,is_active = True,) :
    user_hospitals_id   = get_user_hospitals_id(user ,is_active)
    user_roles_id       = get_user_roles_id(user , is_active)
    user_roles_names    = get_user_roles_name(user_roles_id)

    print(user_roles_names.values("name",))
    # Its For That The User Can Have Just one role :
    if  user_roles_names.filter(name__in = ["SuperAdmin",]).exists(): 
        ALLOWED_LIST = SUPER_ADMIN_ALLOWED_LIST
    elif user_roles_names.filter(name__in = ["Admin" ,]).exists() :
        ALLOWED_LIST = ADMIN_ALLOWED_LIST
    elif user_roles_names.filter(name__in = ["Doctor"]).exists() : 
        ALLOWED_LIST = DOCTOR_ALLOWED_LIST

    print(ALLOWED_LIST)
    
    # query = user.userHospitals.filter(
    #     role__name__in = ALLOWED_LIST ,
    #     hospital__id__in = 
    # )
    query = get_user_model().objects.filter(
        userHospitals__hospital_id__in  = user_hospitals_id ,
        userHospitals__role__name__in    = ALLOWED_LIST ,

    ).distinct()
    return query
    