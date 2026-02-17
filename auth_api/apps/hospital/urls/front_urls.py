from django.urls import path
from auth_api.apps.hospital.views.front_views import ( HospitalMemberShipsAPIView , 
                                                       UserHospitals , 
                                                       UserHospitalDetails
                                                    )
# create Your Urls : 

urlpatterns = [

    path("<int:hospital_id>/members/" , HospitalMemberShipsAPIView.as_view()) , 

    path("all/" , UserHospitals.as_view()) ,
    path("<int:hospital_id>/details/" , UserHospitalDetails.as_view() ) , 

]
