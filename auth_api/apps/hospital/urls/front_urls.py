from django.urls import path
from auth_api.apps.hospital.views import HospitalMemberShipsAPIView
# create Your Urls : 

urlpatterns = [
    path("<int:hospital_id>/members/" , HospitalMemberShipsAPIView.as_view())
    
    
]
