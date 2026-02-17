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
from auth_api.auth.account.queries.admin_queries import (user_role_in_hospital , get_user_hospitals_id)


# Create Your Departement Queries : 

def get_user_departement(user) : 
    
    query = Departement.objects.filter(departements__user =user)

    return query