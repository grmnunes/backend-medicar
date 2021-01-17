from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


from consultation.views import ConsultationViewSet
from doctor.views import DoctorViewSet
from especiality.views import EspecialityViewSet
from schedule.views import ScheduleViewSet

router = routers.DefaultRouter()

router.register(r'consultas', ConsultationViewSet, basename='Consultation')
router.register(r'medicos', DoctorViewSet, basename='Doctor')
router.register(r'especialidades', EspecialityViewSet, basename='Especiality')
router.register(r'agendas', ScheduleViewSet, basename='Schedule')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'rest-auth/registration/', include('rest_auth.registration.urls'))
]
