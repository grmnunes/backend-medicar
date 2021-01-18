from django.contrib import admin

from .models import Schedule, ScheduleHour


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
  list_display = ('doctor', 'day', 'id')
  list_filter = ('doctor', 'day')

@admin.register(ScheduleHour)
class ScheduleHourAdmin(admin.ModelAdmin):
  list_display = ('schedule', 'hour', 'id')
  list_filter = ('hour',)


