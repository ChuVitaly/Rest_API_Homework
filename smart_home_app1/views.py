from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from smart_home_app1.models import Facility, Measurement
from smart_home_app1.serializers import FacilitySerializer, MeasurementSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer