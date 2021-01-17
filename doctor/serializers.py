from rest_framework import serializers

from .models import Doctor
from especiality.serializers import EspecialitySerializer


class DoctorSerializer(serializers.ModelSerializer):
    especiality = EspecialitySerializer(read_only=True)

    class Meta:
        extra_kwargs = {
            'email' : {'write_only': True},
            'phone' : {'write_only': True}
        }
        model = Doctor
        fields = (
            'id',
            'crm',
            'name',
            'especiality',
        )