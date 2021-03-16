from rest_framework import serializers
from authApp.models import Hotel,Guest,Reservation
import re
 
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields='__all__'
    
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields='__all__'

    def validate_firstName(self,firstName):
        if(re.match("^[a-zA-Z0-9]*$", firstName)==None):  
            raise serializers.ValidationError("Invalid name. Make sure name only contains letters and numbers")
        return firstName

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'