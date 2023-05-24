from rest_framework import generics


from smart_home.smart_home_app1.models import Sensor, Measurement
from smart_home.smart_home_app1.serializers import SensorSerializer, MeasurementSerializer


class SensorList(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementList(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetail(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer