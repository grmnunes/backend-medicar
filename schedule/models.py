from django.db import models
from datetime import date
import time

from doctor.models import Doctor
from .validators import validate_schedule_day


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Médico', related_name='doctor', on_delete=models.CASCADE)
    day = models.DateField('Dia', validators=[validate_schedule_day])
    is_completed = models.BooleanField(verbose_name='Agenda completa', default=False, editable=False)
    
    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        unique_together = ['doctor', 'day']
        ordering = ['day']

    def __str__(self):
        return f"{self.doctor.name} | {self.day.strftime('%d/%m/%Y')}"


class ScheduleHour(models.Model):
    schedule = models.ForeignKey(Schedule, verbose_name='Agenda',related_name='schedule', limit_choices_to = {'day__gte': date.today()}, on_delete=models.CASCADE)
    hour = models.TimeField(verbose_name='Hora', help_text='O horário deve conter apenas horas e minutos ex.: 12:45')
    is_available = models.BooleanField(verbose_name='Disponível', default=True, editable=False)
    
    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Hórarios'
        unique_together = ['schedule', 'hour']
        ordering = ['-hour']

    def __str__(self):
        return f'{self.hour}'
