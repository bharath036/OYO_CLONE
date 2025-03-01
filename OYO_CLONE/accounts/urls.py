from django.urls import path
from accounts.views import login_page , register,verify_email_token,send_otp,verify_otp,login_vendor,register_vendor,dashboard,add_hotel,upload_images,delete_image, edit_hotel,logout_view

urlpatterns = [
    path('login/',login_page,name="login_page"),
    path('register/',register,name= 'register_page'),
    path('send_otp/<str:email>/',send_otp,name= 'send_otp'),
    path('verify-otp/<str:email>/',verify_otp,name= 'verify_otp'),

    #path('send_otp/<str:email>/',send_otp,name= 'send_otp'),
    path('login-vendor/',login_vendor,name= 'login_vendor'),
    path('register-vendor/',register_vendor,name= 'register_vendor'),
    path('dashboard/',dashboard,name="dashboard"),
    path('add-hotel/',add_hotel,name="add_hotel"),
    path('<slug>/upload-images/',upload_images,name="upload_images"),
    path('delete_image/<id>/',delete_image,name="delete_image"),
    path('edit-hotel/<slug>/',edit_hotel,name="edit_hotel"),

    path('logout_view/',logout_view,name='logout_view'),

    path('verify-account/<token>/',verify_email_token,name="verify_email_token")
]