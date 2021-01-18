from rest_framework import serializers

from .models import Especiality


class EspecialitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especiality
        fields = (
            'id',
            'name',
        )
        