from django.core.exceptions import ValidationError
from datetime import date, datetime


def validate_schedule_day(date):

    if date < date.today():
        raise ValidationError("Sinto muito, mas não é possível cadastrar agendas com datas anteriores a hoje.")
    
    return date
    

def validate_schedule_hour(hour):

    if hour.strftime('%H:%M') < datetime.now().strftime('%H:%M'):
       raise ValidationError("Sinto muito, mas não é possível cadastrar horários passados na agenda.")
    
    print(f'%%%%%%%%{hour}%%%%%%%%')
    
