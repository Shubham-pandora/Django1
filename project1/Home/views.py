from cgitb import html
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'build':"build-Number",
        'ip':"10.30.48.163"
    }
    # return HttpResponse("this is message")
    return render(request,'index.html',context)


def about(request):
    context = {
        'build':"build-Number",
        'ip':"10.30.48.163"
    }
    return render(request,'about.html',context)

def services(request):
    if request.method == "POST":
        BuildNumber = request.POST.get('buildno')            
        ipAdd = request.POST.get('ipaddress')
        print("hiiiiiiiiiiiiiiii")
        print(BuildNumber,ipAdd)
        messages.success(request, 'Your message has been sent.')
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')            
        Email = request.POST.get('email')
        contact = Contact(name='Name',email='Email',date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
