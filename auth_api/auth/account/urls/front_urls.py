from django.urls import path
from auth_api.auth.account.views.front_views import (
    
    UserProfile ,
    UserListAPIView,
    UserDetailsByIdAPIView, 
                                                        )
from auth_api.auth.account.views.back_views import (
     AddUser ,

)

# Create Your URLS
urlpatterns = [
    path("profile/" , UserProfile.as_view() ) ,

    path("user-list/<int:hospital_id>/" , UserListAPIView.as_view()) ,

    path("user-details/<int:user_id>/" , UserDetailsByIdAPIView.as_view()) , 

    path("add-user/" , AddUser.as_view()) ,
    


    
]
