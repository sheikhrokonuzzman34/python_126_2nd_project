from django.shortcuts import render

# Create your views here.re

def index(request):
    return render(request,'mainapp/index.html')


def contact(request):
    return render(request,'mainapp/contact.html')
    
