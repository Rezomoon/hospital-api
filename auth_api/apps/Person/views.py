from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
 
class PatientsInSpecifiedHospitals(APIView) : 
    def get(self, request, hospital_id) :
        pass
