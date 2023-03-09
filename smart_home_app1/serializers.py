from rest_framework import serializers

from smart_home_app1.models import Facility, Measurement

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['name', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['value', 'facility', 'created_at', 'updated_at']