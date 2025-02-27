from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class HotelUser(User):
    profile_picture = models.ImageField(upload_to='profile')
    phone_number = models.CharField(max_length=10,unique=True)
    email_token = models.CharField(max_length=100,null = True,blank = True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    #False means email not verified
    is_verified = models.BooleanField(default=False)

class Hotelvendor(User):
    phone_number = models.CharField(max_length=10,unique=True)
    profile_picture = models.ImageField(upload_to='profile')
    email_token = models.CharField(max_length=100,null = True,blank = True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    is_verified = models.BooleanField(default=False)

#Now we are creating hotel model 

class Ameneties(models.Model):
    #amanetie names like AC,WIFI,SWIMMING POOL
    name = models.CharField(max_length=1000)
    icon = models.ImageField(upload_to="hotels")

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_slug = models.SlugField(max_length=1000,unique=True)
    hotel_owner = models.ForeignKey(Hotelvendor,on_delete=models.CASCADE,related_name="hotels")
    ameneties = models.ManyToManyField(Ameneties)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default=True)
    

class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotel_images")
    image = models.ImageField(upload_to="hotels")

class HotelManager(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotel_manager")
    manager_name = models.CharField(max_length=100)
    manager_contact = models.CharField(max_length=100)


