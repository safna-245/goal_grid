from datetime import datetime

from rest_framework import serializers

from django.contrib.auth.models import User

from playslot_v2.models import Bookings_v2

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class BookingSerializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()

    class Meta:

        model = Bookings_v2

        fields = "__all__"

        read_only_fields = ["end_time"]

    def validate(self, validated_data):

        date = validated_data.get("date")
        time = validated_data.get("time")
        turf = validated_data.get("turf")

        if date < datetime.today().date():
            
            raise serializers.ValidationError("invalid date.date should be greater than current date")
        

        bookings = Bookings_v2.objects.filter(date=date,turf=turf)

        for booking in bookings:

            if booking.time <= time < booking.end_time:
                raise serializers.ValidationError("This turf is already booked.")

        return validated_data