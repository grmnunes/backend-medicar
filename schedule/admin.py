from django.contrib import admin

from .models import Schedule, ScheduleHour


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
  list_display = ('id', 'doctor', 'day')
  list_filter = ('doctor', 'day')


@admin.register(ScheduleHour)
class ScheduleHourAdmin(admin.ModelAdmin):
  list_display = ('id', 'schedule', 'hour', 'is_available')
  list_filter = ('schedule', 'hour', 'is_available')
