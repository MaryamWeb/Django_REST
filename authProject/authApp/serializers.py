from rest_framework import serializers
from authApp.models import Hotel,Guest,Reservation
 
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields='__all__'
    
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'