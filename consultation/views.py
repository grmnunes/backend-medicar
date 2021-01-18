from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from datetime import date, datetime

from .models import Consultation
from schedule.models import ScheduleHour
from schedule.models import Schedule
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from schedule.serializers import ScheduleSerializer
from .serializers import ConsultationSerializer
from .validators import validate_schedule, validate_schedule_hour


class ConsultationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        consultations = (Consultation.objects.exclude(status='C')
                            .exclude(status='R')
                            .filter(patient=request.user.id)
                            .filter(day__gte=date.today())
                            .filter(schedule__hour__gte=datetime.now().strftime('%H:%M'))
                            .order_by('day','schedule__hour')
                        )

        serializer = ConsultationSerializer(consultations, many=True)

        return Response(serializer.data)


    def destroy(self, request, pk):
        
        try:
            consultation = Consultation.objects.get(pk=pk)
        
        except Consultation.DoesNotExist:
            raise ValidationError({"status_code": 400, "detail": "Consulta não encontrada."})


        if consultation.patient == request.user:
            print('Consulta pertence ao usuario')
        else:    
            raise ValidationError({"status_code": 401, "detail": "Não é possivel atender sua solitação."})
        
        schedule = Schedule.objects.get(pk=consultation.schedule.schedule.id)
       
        if schedule.day < date.today() or consultation.status == 'R' or consultation.status == 'C':
            raise ValidationError(detail='Não é mais possível desmarcar esta consulta.')    
            
        schedule_hour = ScheduleHour.objects.get(pk=consultation.schedule.id)
        consultation.status = 'C'
        schedule_hour.is_available = True
        schedule_hour.save()
        consultation.save()
        schedule.is_completed = False
        schedule.save()

        return Response(None)
