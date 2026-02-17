from rest_framework import serializers
from auth_api.apps.Person.models import *
# Create Your Serializers :

class PateintSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model   = Patient
        fields  = "__all__"

class VisitSerializers(serializers.ModelSerializer) :
    class Meta : 
        model = Visit 
        fields = "__all__"
