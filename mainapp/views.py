from django.shortcuts import render

# Create your views here.re

def index(request):
    return render(request,'index.html')
    
