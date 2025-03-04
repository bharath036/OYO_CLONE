from django.db import models
from django.contrib.auth.models import User 
#if we import generateSlug here from utils.py we get circular error as in 
#utils.py we are importing Hotel model
#So we import in hotel class inside save function
#from .utils import generateSlug
# Create your models here.

class HotelUser(User):
    profile_picture = models.ImageField(upload_to='profile')
    phone_number = models.CharField(max_length=10,unique=True)
    email_token = models.CharField(max_length=100,null = True,blank = True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    #False means email not verified
    is_verified = models.BooleanField(default=False)
    #otp = models.CharField(max_length=10,null=True,blank=True)
    # 
    class Meta:
        db_table = "hotel_user" 

class Hotelvendor(User):
    phone_number = models.CharField(max_length=10,unique=True)
    business_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile')
    email_token = models.CharField(max_length=100,null = True,blank = True)
    otp = models.CharField(max_length=10,null=True,blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = "hotel_vendor" 

#Now we are creating hotel model 

class Ameneties(models.Model):
    #amanetie names like AC,WIFI,SWIMMING POOL
    name = models.CharField(max_length=191)
    icon = models.ImageField(upload_to="hotels")

    def __str__(self):
        return self.name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_slug = models.SlugField(max_length=191,unique=True)
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

class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="bookings")
    booking_user = models.ForeignKey(HotelUser,on_delete=models.CASCADE,)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    price = models.FloatField()
