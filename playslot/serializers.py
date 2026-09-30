from rest_framework import serializers

class BookingSerializer(serializers.Serializer):

    booked_by = serializers.CharField()

    phone = serializers.CharField()

    date = serializers.DateField()

    turf = serializers.IntegerField()

    time = serializers.TimeField()

    duration = serializers.IntegerField()

    





