from django.contrib.auth import get_user_model
from auth_api.auth.account.models import (Role)
from rest_framework.response import Response
from rest_framework import status 
from django.db.models import Q
from auth_api.utils.utils import check_roles
# Create Your Queries : 

def get_user(id) : 
    """
    Docstring for get_user
    
    :param id: User Id For Get The User Query
    """
    try :
        user = get_user_model().objects.get(id = id)
        return user
    except get_user_model().DoesNotExist :
        return Response({"errors" : "USER DOESE NOT EXIST!"} , status=status.HTTP_404_NOT_FOUND)
def get_user_by_email(email) :
    try :
        user = get_user_model().objects.get(email = email)
        return user
    except get_user_model().DoesNotExist :
        return Response({"errors" : "USER DOESE NOT EXIST!"} , status=status.HTTP_404_NOT_FOUND)
    

def get_user_hospitals_id(user , is_active = True) : 
    """
    Docstring for get_user_hospitals_id
    
    :param user: request.user
    :param is_active: Its Default active

    this function retrun the active user's hospitals

    """

    query = user.userHospitals.filter(is_active = is_active).values_list("hospital_id" , flat = True)

    return query

def get_role_hospitals_id(user , role, is_active = True) : 
    """
    Docstring for get_role_hospitals_id
    
    :param user: request.user
    :param role: it set the role of user
    :param is_active: it return active user's hospitals 
    This query return the hospitals the user is active on theme with the specified Role !

    """
    query = user.userHospitals.filter(is_active = is_active , role__name = role)

    return query

def get_user_roles_id(user , is_active = True) :
    """
    Docstring for get_user_roles_id
    
    :param user: request.user
    :param is_active: default is active

    This Query return the user's role's Id s

    """

    query = user.userHospitals.filter(is_active = is_active ).values_list("role_id" , flat = True)

    return query

def get_user_roles_name(user_roles_id) :
    """
    Docstring for get_user_roles_name
    
    :param user_roles_id: it get a list of users id 
    This Query Return The User's Role Names !
    """

    query = Role.objects.filter(id__in = user_roles_id)

    return query

def user_role_in_hospital(user,hospital_id, is_active = True) : 
    """
    Docstring for user_role_in_hospital
    
    :param user: request.user
    :param hospital_id: The Specified Hospital Id
    :param is_active: Set is This User on This Hospital is active or not
    It Returns the roles Name of user that are in the Specified Hospital

    """
    query = user.userHospitals.filter(is_active = is_active , hospital_id = hospital_id).values_list("role__name",flat = True)
    return query



def get_user_list_by_hospital_id(user,hospital_id,is_active = True,) :
    """
    Docstring for get_user_list_by_hospital_id
    
    :param user: get request.user
    :param hospital_id: get hospital_id(for ex :from url)
    :param is_active: it say the roles that there are still active 
    It Return the Users that are in the specified Hospital 
    ! the roles !
    """
    
    # user_hospitals_id   = get_user_hospitals_id(user ,is_active)
    # user_roles_names    = get_user_roles_name(user_roles_id)
    # user_roles_id       = get_user_roles_id(user , is_active)

    # TODO : I Shoul Daynamic and check user role

    user_role           = user_role_in_hospital(user , hospital_id , is_active)

    allowed_list = check_roles(user_role)

    query = get_user_model().objects.filter(
        Q(userHospitals__hospital_id = hospital_id) 
        &
        Q(userHospitals__role__name__in = allowed_list)
    ).distinct()

    return query
    