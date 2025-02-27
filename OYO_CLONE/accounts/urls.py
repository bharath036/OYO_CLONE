from django.urls import path
from accounts.views import login_page , register,verify_email_token

urlpatterns = [
    path('login/',login_page,name="login_page"),
    path('register/',register,name= 'register_page'),
    path('verify-account/<token>/',verify_email_token,name="verify_email_token")
]