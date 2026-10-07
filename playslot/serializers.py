from rest_framework import serializers
from playslot.models import Turf
class BookingSerializer(serializers.Serializer):

    booked_by = serializers.CharField()

    phone = serializers.CharField()

    date = serializers.DateField()

    turf = serializers.PrimaryKeyRelatedField(queryset=Turf.objects.all())

    time = serializers.TimeField()

    duration = serializers.IntegerField()

    





