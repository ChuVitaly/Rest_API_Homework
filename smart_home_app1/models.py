from django.db import models

class Facility(models.Model):

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Measurement(models.Model):

    value = models.FloatField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )