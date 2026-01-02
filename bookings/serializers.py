from rest_framework import serializers
from .models import Seat,Bus,Booking
from django.contrib.auth.models import User


class SignUpSerializers(serializers.ModelSerializer):
    password  = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def validate_password(self, data):
        if len(data) < 8:
            raise serializers.ValidationError('Password must be atleast 8 characters!')
        elif not any(c.isdigit() for c in data):
            raise serializers.ValidationError('Password must contain atleast one digit.')
        elif not any(c.isupper() for c in data):
            raise serializers.ValidationError('Password must contain atleast one upper case character.')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = (
            'id',
            'bus_name',
            'bus_code',
            'origin',
            'destination',
            'price',
            'features',
            'start_time',
            'reach_time'
        )


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'id',
            'seat_no',
            'is_booked'
        )

class BookingSerializers(serializers.ModelSerializer):
    bus = serializers.StringRelatedField()
    seat = SeatSerializer
    user = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ['user','booking_at','bus','seat']