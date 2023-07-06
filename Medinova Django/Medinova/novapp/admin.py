from django.contrib import admin
from novapp.models import Appoinment
# Register your models here.

@admin.register(Appoinment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','department','doctor','email','date']