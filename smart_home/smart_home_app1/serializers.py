from rest_framework import serializers

from smart_home.smart_home_app1.models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'sensor', 'created_at', 'updated_at']