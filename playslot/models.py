from django.db import models

from kickora.models import Turf

# Create your models here.
class Bookings(models.Model):

    booked_by = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    date = models.DateField()

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    time = models.TimeField()

    duration = models.PositiveIntegerField()