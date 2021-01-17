from django.db import models
from django.core.validators import EmailValidator

from especiality.models import Especiality


class Doctor(models.Model):
  
    name = models.CharField('Nome', max_length=255)
    crm = models.CharField('CRM', max_length=10, unique=True,)
    email = models.EmailField('E-mail', validators=[EmailValidator], unique=True, null=True, blank=True)
    phone = models.CharField('Telefone', max_length=14, null=True, blank=True)
    especiality = models.ForeignKey(Especiality, related_name='especialitiy', verbose_name='Especialidade', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Médico(a)'
        verbose_name_plural = 'Médicos(as)'
        ordering = ['-created']

    def __str__(self):
        return self.name

