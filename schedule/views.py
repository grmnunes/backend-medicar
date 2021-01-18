from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from datetime import date
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Schedule, ScheduleHour
from .serializers import ScheduleSerializer



class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Schedule.objects.filter(day__gte=date.today()).filter(is_completed='False')
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctor','day']

    