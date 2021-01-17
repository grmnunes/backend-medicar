from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from datetime import date

from .models import Schedule, ScheduleHour
from .serializers import ScheduleSerializer



class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Schedule.objects.filter(day__gte=date.today()).filter(is_completed='False')
    #schedule_hours = ScheduleHour.objects.all()
    serializer_class = ScheduleSerializer
    