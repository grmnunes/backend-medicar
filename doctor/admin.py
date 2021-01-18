from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

from .models import Doctor

admin.site.unregister(Group)
admin.site.unregister(Site)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ('name', 'crm', 'especiality', 'is_active')
