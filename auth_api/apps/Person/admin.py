from django.contrib import admin
from .models import Role , Status
# Register your models here.



class RoleModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Role, RoleModelAdmin)

class StatusModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Status , StatusModelAdmin)
