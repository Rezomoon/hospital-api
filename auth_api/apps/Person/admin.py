from django.contrib import admin
from .models import  Status
# Register your models here.


class StatusModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Status , StatusModelAdmin)
