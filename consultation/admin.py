from django.contrib import admin

from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = (
        'scheduling_date',
        'patient',
        'day',
        'id',
    )
