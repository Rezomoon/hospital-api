from django.contrib import admin
from .models import Patient , Visit
from auth_api.auth.account.admin import BaseCustomUserAdminModel
# Register your models here.


@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin) : 
    list_display    = ("id",  "full_name", "person_code"
                        ,"is_active", "status", "gender",
                        "get_hospital" ,
                        # "get_departement" ,
                          )
    list_filter     = ("is_active", "status", "gender",)
    search_fields = ("first_name", "last_name",)
    ordering = ("first_name", "last_name")

    get_hospital = BaseCustomUserAdminModel.get_hospital
    # get_departement = BaseCustomUserAdminModel.get_departement

class VisitAdminModel(admin.ModelAdmin) : 
    list_display    = [ "id", "doctor", "patient", "hospital", "departement", "description",  "visit_date"]
admin.site.register(Visit , VisitAdminModel)