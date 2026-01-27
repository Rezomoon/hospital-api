from django.urls import path
from auth_api.auth.account.views.back_views import UserRegistration ,LoginAPI

# Create Your URLS
urlpatterns = [
    path("register/" , UserRegistration.as_view() ) ,
    path("login/" , LoginAPI.as_view() ),
]
