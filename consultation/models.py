from django.db import models

from doctor.models import Doctor
from schedule.models import ScheduleHour
from patient.models import Patient

class Consultation(models.Model):
    STATUS_CHOICES = (
        ('M','MARCADA'),
        ('R','REALIZADA'),
        ('C','CANCELADA'),
    )

    patient = models.ForeignKey(Patient, verbose_name='Paciente', related_name='consultations', on_delete=models.CASCADE)
    scheduling_date = models.DateTimeField(verbose_name='Data do agendamento', auto_now_add=True)
    doctor = models.ForeignKey(Doctor, related_name='consultations', verbose_name='Médico', on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(ScheduleHour, related_name='consultations', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='M')
    day = models.DateField(verbose_name='Dia da consulta')

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['-day']


    def __str__(self):
        return f'Consulta com {self.doctor.name} em {self.scheduling_date}'
        