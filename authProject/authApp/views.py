from django.shortcuts import render
from authApp.models import Hotel,Guest,Reservation
from authApp.serializers import HotelSerializer,GuestSerializer,ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def find_hotels(request):
    hotels = Hotel.objects.filter(country =request.data['country'], city=request.data['city'])
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    hotel = Hotel.objects.get(id=request.data['hotelId'])
    guest = Guest()
    guest.firstName = request.data['firstName']
    guest.lastName = request.data['lastName']
    guest.email = request.data['emaill']
    guest.phone = request.data['phone']
    guest.save()
    reservation = Reservation()
    reservation.hotel=hotel
    reservation.guest=guest
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

class HotelViewSet(viewsets.ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    permission_classes = (IsAuthenticated, )
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer