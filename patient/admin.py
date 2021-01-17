from django.contrib import admin

from .models import Patient

@admin.register(Patient)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = 'username',
