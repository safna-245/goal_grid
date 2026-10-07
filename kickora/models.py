from django.db import models
# [id,name,location,phone,fee]
# Create your models here.
class Turf(models.Model):

    name = models.CharField(max_length=200)

    location = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    fee = models.IntegerField()

    def __str__(self):
        
        return self.name

