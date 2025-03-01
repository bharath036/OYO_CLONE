from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(HotelUser)
admin.site.register(Hotelvendor)
#From backend we create logic ameneties
admin.site.register(Ameneties)
admin.site.register(Hotel)
