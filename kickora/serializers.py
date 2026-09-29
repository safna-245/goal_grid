from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()


class TurfSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField()

    location = serializers.CharField()

    phone = serializers.CharField()

    fee = serializers.IntegerField()

    def validate(self,validated_data):

        fee = validated_data.get("fee")

        if fee <= 500:

            raise serializers.ValidationError("fee must be greater than 500")

        return validated_data