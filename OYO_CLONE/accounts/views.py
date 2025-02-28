from django.shortcuts import render, redirect
from .models import HotelUser, Hotelvendor,Hotel
from django.db.models import Q
from django.contrib import messages
from .utils import generateRandomToken,sendEmailToken ,sendOTPtoEmail
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
import random
from django.contrib.auth.decorators import login_required
from .utils import generateSlug

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
    print('Inside login Page')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        hotel_user = HotelUser.objects.filter(email = email)
        
        if not hotel_user.exists():
            messages.error(request , 'No1 Account Found')
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

def send_otp(request,email):
    hotel_user = HotelUser.objects.filter(email=email)
    if not hotel_user.exists():
        messages.warning(request,"No Account Found")
        return redirect('/login')
    otp = random.randint(1000,9999)
    hotel_user.update(otp = otp)
    sendOTPtoEmail(email,otp)

    return redirect(f'/verify-otp/{email}/')

def verify_otp(request,email):
    print("Received email in URL:", email)
    if request.method == "POST":
        otp = request.POST.get('otp')
        print("---otp---",otp)
        hotel_user = HotelUser.objects.get(email=email)

        if str(otp) == str(hotel_user.otp):
            print("-------Hi-------------")
            messages.success(request,"Login Success")
            login(request,hotel_user)
            return redirect('/login')
        
        messages.warning(request,"Wrong OTP")
        return redirect('/verify-otp/{email}/')
    
    return render(request,'verify_otp.html')


#####################################################################################################################################################

#---------------Login and register views for Vendor--------------
def register_vendor(request):
    print('Inside register Page')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        business_name = request.POST.get('business_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        hotel_user = HotelUser.objects.filter(Q(email = email) | Q(phone_number=phone_number))
        
        if hotel_user.exists():
            messages.error(request , 'Account exists with email or phone number')
            return redirect('/register-vendor')
        
        hotel_user = Hotelvendor.objects.create(
            username = phone_number,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            business_name = business_name,
            email_token = generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()

        sendEmailToken(email,hotel_user.email_token)

        messages.success(request , 'Email Sent to your Email')
        return redirect('/register-vendor')

    return render(request,'vendor/register_vendor.html')



def login_vendor(request):
    print('Inside login Page')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        hotel_user = Hotelvendor.objects.filter(email = email)
        
        if not hotel_user.exists():
            messages.error(request , 'No1 Account Found')
            return redirect('/login-vendor')
        
        if not hotel_user[0].is_verified:
            messages.success(request , 'ACCOUNT NOT VERIFIED')
            return redirect('/login-vendor')
        
        
        hotel_user = authenticate(username=hotel_user[0].username,password=password)

        if hotel_user:
            messages.success(request , 'Login successful')
            login(request,hotel_user)
            return redirect('/dashboard')
        
        messages.success(request , 'Invalid credentials')
        return redirect('/login-vendor')

    return render(request,'vendor/login_vendor.html')


######################################################################
#-----------------DASHBOARD-----------------------------------------


@login_required(login_url='login_vendor')
def dashboard(request):
    print('-------------------Hi-------------------')
    if request.method == "POST":
        print("-----------add_hotel---------")
        return redirect('add_hotel')
    return render(request,"vendor/vendor_dashboard.html")

@login_required(login_url='login_vendor')   
def add_hotel(request):
    if request.method == "POST":
        hotel_name = request.POST.get('hotel_name')
        hotel_description = request.POST.get('hotel_description')
        ameneties=request.POST.get('ameneties')
        hotel_price = request.POST.get('hotel_price')
        hotel_office_price = request.POST.get('hotel_office_price')
        hotel_location = request.POST.get('hotel_location')
        hotel_slug = generateSlug(hotel_name)

        Hotel.objects.create(
            hotel_name = hotel_name,
            hotel_description= hotel_description,
            hotel_price = hotel_description,
            hotel_office_price = hotel_office_price,
            hotel_location = hotel_location,
            hotel_slug = hotel_slug
        )
       #return redirect(request,'/dashboard')
    return redirect(request,'vendor/add_hotel.html')
