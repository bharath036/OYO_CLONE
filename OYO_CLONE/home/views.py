from django.shortcuts import render

# Create your views here.

def index(request):
    print('Inside html')
    return render(request,'index.html')

def login_page(request):
    print('Inside login Page')

    return render(request,'login.html')

def register(request):
    print('Inside register Page')

    return render(request,'register.html')
