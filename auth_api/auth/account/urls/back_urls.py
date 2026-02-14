from django.urls import path
from auth_api.auth.account.views.back_views import (UserRegistration, LoginAPI, 
                                                    SentResetPasswordEmail , UserPasswordReset,LogoutUser )

# Create Your URLS
urlpatterns = [
    path("register/" , UserRegistration.as_view() ) ,
    path("login/" , LoginAPI.as_view() ),
    path("logout/" , LogoutUser.as_view()) , 
    
    path("reset-password/" , SentResetPasswordEmail.as_view() ),
    path("reset-password/<uid>/<token>/", UserPasswordReset.as_view()),


]
