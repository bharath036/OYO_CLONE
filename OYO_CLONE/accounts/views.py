from django.shortcuts import render, redirect
from .models import HotelUser
from django.db.models import Q
from django.contrib import messages
from .utils import generateRandomToken,sendEmailToken 
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
'''
def login_page(request):
    print('Inside login Page')

    return render(request,'login.html')
'''


def register(request):
    print('Inside register Page')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        hotel_user = HotelUser.objects.filter(Q(email = email) | Q(phone_number=phone_number))
        
        if hotel_user.exists():
            messages.error(request , 'Account exists with email or phone number')
            return redirect('/register')
        
        hotel_user = HotelUser.objects.create(
            username = phone_number,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            email_token = generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()

        sendEmailToken(email,hotel_user.email_token)

        messages.success(request , 'Email Sent to your Email')
        return redirect('/register')

    return render(request,'register.html')

def verify_email_token(request,token):
    try:
        hotel_user = HotelUser.objects.get(email_token = token)
        hotel_user.is_verified = True 
        hotel_user.save()
        messages.success(request , 'Email verified')
        return redirect('/login')

    except Exception as e:
        return HttpResponse('Invalid Token')
def login_page(request):
    print('Inside register Page')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        hotel_user = HotelUser.objects.filter(email = email)
        
        if not hotel_user.exists():
            messages.error(request , 'No Account Found')
            return redirect('/login')
        
        if not hotel_user[0].is_verified:
            messages.success(request , 'ACCOUNT NOT VERIFIED')
            return redirect('/login')
        
        
        hotel_user = authenticate(username=hotel_user[0].username,password=password)

        if hotel_user:
            messages.success(request , 'Login successful')
            login(request,hotel_user)
            return redirect('/login')
        
        messages.success(request , 'Invalid credentials')
        return redirect('/login')

    return render(request,'login.html')
    
