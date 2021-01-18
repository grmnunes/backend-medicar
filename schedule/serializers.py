from rest_framework import serializers

from .models import Schedule, ScheduleHour
from doctor.serializers import DoctorSerializer


class ScheduleHourSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleHour
        fields = (
            'hour', 
        )

class ScheduleSerializer(serializers.ModelSerializer):
    schedule = serializers.StringRelatedField(many=True)
    doctor = DoctorSerializer()

    class Meta:
        model = Schedule
        fields = (
            'id',
            'doctor',
            'day',
            'schedule',
        )
        depth = 2
        