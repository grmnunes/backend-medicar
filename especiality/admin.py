from django.contrib import admin

from .models import Especiality

@admin.register(Especiality)
class EspecialityAdmin(admin.ModelAdmin):
  list_display = ('name', 'isActive')
