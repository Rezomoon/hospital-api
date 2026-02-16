from rest_framework import serializers 
from auth_api.apps.hospital.models import * 

# Create Your Serializers : 
# Here Is Basics Serializers Models : 

class HospitalSerializers(serializers.ModelSerializer) :
    class Meta  : 
        model   = Hospital 
        fields  = "__all__"

class DepartementSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model   = Departement
        fields  = "__all__"

class UserHospitalMembershipSerializers(serializers.ModelSerializer) : 
    class Meta :
        model   = UserHospitalMembership
        fields  = "__all__"

class PatientAdmissionSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model   = PatientAdmission
        fields  = "__all__"
