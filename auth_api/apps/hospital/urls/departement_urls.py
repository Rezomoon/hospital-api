from django.urls import path
from auth_api.apps.hospital.views.departement_views import UserDeopartements
# Craete Your departement urls :

urlpatterns = [
    path("all/" , UserDeopartements.as_view() ,)
]
