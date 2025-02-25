from django.urls import path
from home.views import index, login_page , register

urlpatterns = [
    path('', index ,name='index'),
    path('login/',login_page,name="login_page"),
    path('register/',register,name= 'register_page')
]
