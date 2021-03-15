from django.shortcuts import render
from authApp.models import Hotel,Guest,Reservation
from authApp.serializers import HotelSerializer,GuestSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def find_hotels(request):
    hotels = Hotel.objects.filter(country =request.data['country'], city=request.data['city'])
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

class HotelViewSet(viewsets.ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer