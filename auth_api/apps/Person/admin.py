from django.contrib import admin
from .models import Patient , Visit
from auth_api.auth.account.admin import BaseCustomUserAdminModel
# Register your models here.



class InLinePatient(admin.TabularInline) :
    model   = Patient.admission.through
    fk_name = "patient"
@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin) : 
    list_display    = ("id",  "full_name", 
                        "is_active", "status", 
                        "gender",
                        # "admission" ,
                        #  "person_code" ,
                        "get_hospital" ,
                        # "get_departement" ,
                          )
    list_filter     = ("is_active", "status", "gender",)
    search_fields = ("first_name", "last_name",)
    ordering = ("first_name", "last_name")
    
    inlines         = [InLinePatient]

    def get_hospital(self , obj) :
        return [admission.name   for admission in obj.admission.all()]
    get_hospital.short_description = "Hospital"
    # get_departement = BaseCustomUserAdminModel.get_departement

class VisitAdminModel(admin.ModelAdmin) : 
    list_display    = [ "id", "doctor", "patient", "hospital", "departement", "description",  "visit_date"]
admin.site.register(Visit , VisitAdminModel)