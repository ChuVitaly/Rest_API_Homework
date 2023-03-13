from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from smart_home_app1.models import Sensor, Measurement
from smart_home_app1.serializers import SensorSerializer, MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer