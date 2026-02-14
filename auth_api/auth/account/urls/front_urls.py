from django.urls import path
from auth_api.auth.account.views.front_views import UserProfile

# Create Your URLS
urlpatterns = [
    path("profile/" , UserProfile.as_view() ) ,
    
]
