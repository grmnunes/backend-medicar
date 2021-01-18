from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import filters

from .models import Especiality
from .serializers import EspecialitySerializer


class EspecialityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Especiality.objects.all()
    serializer_class = EspecialitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']
