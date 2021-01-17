from django.db import models

class Especiality(models.Model):
    name = models.CharField('Nome', max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField('Ativo', default=True)

    class Meta:
        
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

