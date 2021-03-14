from django.shortcuts import render
from authApp.models import Hotel,Guest,Reservation
from authApp.serializers import HotelSerializer,GuestSerializer,ReservationSerializer
from rest_framework import viewsets

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer