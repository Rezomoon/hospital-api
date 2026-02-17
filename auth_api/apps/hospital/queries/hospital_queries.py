from django.contrib.auth import get_user_model
from auth_api.apps.hospital.models import (
    Hospital , 
    UserHospitalMembership ,
    Departement , 
    PatientAdmission ,
)
from rest_framework.response import Response
from rest_framework import status 
from django.db.models import Q
from auth_api.utils.utils import check_roles
from auth_api.auth.account.queries.admin_queries import user_role_in_hospital

# Create Your Hospital Apps Queries : 

def get_hospital_by_id(hospital_id) : 
    """
    Docstring for get_hospital_by_id
    
    :param hospital_id: The Specified Hospital's Id 

    """

    try : 
        query = Hospital.objects.get(id = hospital_id)
        return query
    except : 
        return Response({"errors" : "USER DOESE NOT EXIST!"} , status=status.HTTP_404_NOT_FOUND)

def get_UserHospitalMembership_by_hospital_id(user , hospital_id, is_active = True) :
    """
    Docstring for get_UserHospitalMembership_by_hospital_id
    
    :param user: request.user
    :param hospital_id: specified hospital id 
    :param is_active: is the membership active or no !
    It return query from MemberShip Table That is active and with specifed hospital and check the roles of the member ships that should be downer in the chart !
    
    """

    user_role = user_role_in_hospital(user , hospital_id ,is_active)

    allowed_list = check_roles(user_role)

    query = UserHospitalMembership.objects.filter(Q(is_active = True)
                                                  &
                                                  Q(hospital = hospital_id) 
                                                  &
                                                  Q(role__name__in = allowed_list)
                                                  )

    return query