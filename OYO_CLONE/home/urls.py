from django.urls import path
from home.views import index,hotel_details

urlpatterns = [
    path('', index ,name='index'),
    path('hotel-details/<slug>/',hotel_details, name="hotel_details")
]
