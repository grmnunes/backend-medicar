from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime
from rest_framework.exceptions import ValidationError

from .models import Consultation
from patient.serializers import PatientSerializer
from schedule.models import Schedule, ScheduleHour
from doctor.serializers import DoctorSerializer
from schedule.serializers import ScheduleHourSerializer

from .validators import validate_schedule, validate_schedule_hour


class ConsultationSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer(read_only=True)
    schedule = ScheduleHourSerializer(read_only=True)
    day = serializers.DateField(read_only=True)

    class Meta:
        model = Consultation
        fields = (
            
            'id',
            'patient',
            'scheduling_date',
            'day', 
            'doctor',
            'schedule',
            
            
        )
        extra_kwargs = {
            'doctor': {'read_only': True},
            'schedule': {'read_only': True},
            'patient': {'read_only': True},
        } 
        
    def validate(self, data):

        schedule_id  = self.context['request'].data['agenda_id']
        hour_request = self.context['request'].data['horario']
        schedule_hour = None

        if hour_request < datetime.now().strftime('%H:%M'):
            raise ValidationError({"status_code": 401, "detail": "Sinto muito, mas não é possível cadastrar uma consulta com horários passados."})

        if validate_schedule(schedule_id):

            schedule = Schedule.objects.get(pk=schedule_id)
            day = schedule.day

        else:
            raise ValidationError({'error':'Sinto muito, mas a agenda selecionada é invalida'})

        user_consultations = (Consultation.objects
                        .filter(patient=self.context['request'].user)
                        .filter(day=day)
                        .filter(schedule__hour=hour_request)
                        .exclude(status='C')
                        .exclude(day__lt=date.today())
                    ).count()

        if user_consultations:
            raise ValidationError({"status_code": 401, "detail": "O paciente já uma consulta marcada nesse dia/hora."})

        schedule_hours = ScheduleHour.objects.filter(schedule=schedule.id).filter(is_available=True)
        
        try:
            
            schedule_hour = schedule_hours.get(hour=hour_request)
            print(f'{schedule_hour.hour} == {hour_request}')

        except ScheduleHour.DoesNotExist:

            raise ValidationError({"status_code": 401, "detail": "Sinto muito, mas o horário selecionado não está disponivel nesta agenda."})


        if len(schedule_hours) == 1 and schedule_hour != None:

            schedule.is_completed = True
            schedule.save()

       
        patient = self.context['request'].user
        doctor = schedule.doctor
        day = schedule.day
        scheduling_date = datetime.now()
        hour = self.context['request'].data['horario']

        consultation = {
            'patient':patient,
            'scheduling_date':scheduling_date,
            'doctor':doctor,
            'schedule':schedule_hour,
            'day': day,
        }

        if consultation:

            schedule_hour.is_available = False
            schedule_hour.save()
           
            return consultation
        else:
            raise ValidationError("Illegal parameters") #Response({'msg':'Sinto muito, mas o horário selecionado não está disponivel nesta agenda.'}, status.HTTP_400_BAD_REQUEST)
        
    def create(self, validated_data):
    
        #print(validated_data['patient'])
        validated_data
        consultation = Consultation.objects.create(
                                                patient=validated_data['patient'],
                                                scheduling_date=validated_data['scheduling_date'],
                                                doctor=validated_data['doctor'],
                                                schedule=validated_data['schedule'],
                                                day=validated_data['day']
                                                
                                            ) 
        return consultation
    