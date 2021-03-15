from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotelName   = models.CharField(max_length=30) 
    country     = models.CharField(max_length=20)
    city        = models.CharField(max_length=20)
    hotelPhone  = models.CharField(max_length=10)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    #blank=True --> allow blank fields
    #null=True --> allow null values

    def __str__(self):
        return f'<Hotel Name:{self.hotelName}>'

class Guest(models.Model):
    firstName   = models.CharField(max_length=20)
    lastName    = models.CharField(max_length=20)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=10)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'<Guest First Name:{self.firstName}>'

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    guest = models.OneToOneField(Guest,on_delete=models.CASCADE)
