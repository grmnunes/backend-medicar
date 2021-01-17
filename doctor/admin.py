from django.contrib import admin

from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ('name', 'crm', 'especiality', 'is_active')
