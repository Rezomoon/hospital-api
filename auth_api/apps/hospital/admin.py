from django.contrib import admin
from .models import Hospital , Departement, UserHospitalMembership  
# Register your models here.



class HospitalAdminModel(admin.ModelAdmin) : 
    list_display    = ["name", "code", "is_active"]
admin.site.register(Hospital , HospitalAdminModel)


class DepartementAdminModel(admin.ModelAdmin) : 
    list_display    = ["name", "code", "is_active", "hospital"]

admin.site.register(Departement ,DepartementAdminModel )



class UserHospitalMembershipAdminModel(admin.ModelAdmin) : 
    list_display = ["user", "hospital", "departement", "role", "is_active", "joined_at"]
admin.site.register(UserHospitalMembership , UserHospitalMembershipAdminModel)



