from django.shortcuts import render

# Create your views here.

def index(request):
    print('Inside html')
    return render(request,'index.html')


