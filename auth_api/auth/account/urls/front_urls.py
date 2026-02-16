from django.urls import path
from auth_api.auth.account.views.front_views import (UserProfile , UserListAPIView)

# Create Your URLS
urlpatterns = [
    path("profile/" , UserProfile.as_view() ) ,
    path("user-list/" , UserListAPIView.as_view()) ,
    
]
