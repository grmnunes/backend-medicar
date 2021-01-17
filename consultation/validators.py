from django.core.exceptions import ValidationError
from datetime import date

from schedule.models import Schedule


def validate_schedule(schedule_id):

    schedule = Schedule.objects.filter(pk=schedule_id).first()

    if schedule:
        if schedule.day < date.today():
            return False
    else:
        return False
    return True


def validate_schedule_hour(schedule_hours, horario):
    
    for hour in schedule_hours:
            if hour.hour.strftime('%H:%M') == horario and hour.is_available:
                hour.is_available = False
                hour.save()
                scheduling_hour = hour.hour.strftime('%H:%M')
                

                return True
    return False
