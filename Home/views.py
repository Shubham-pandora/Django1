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
        'ip':"IP"
    }
    # return HttpResponse("this is message")
    return render(request,'index.html',context)

def output(request):
   msg1=request.GET.get('buildno')
   msg2=request.GET.get('ipaddress')
   print(msg1,msg2)
   context = {
       'msg1':msg1,
       'msg2':msg2
   }        

   return render(request, 'output.html',context)
#    return render(request, 'output.html',{'msg1':msg1})

# def output(request):
#    msg=request.GET.get('message')
#    print(msg)
#    return render(request, 'output.html',{'msg':msg })

def about(request):
    context = {
        'build':"build-Number",
        'ip':"10.30.48.163"
    }
    return render(request,'about.html',context)

def services(request):
   build1=request.GET.get('buildno')
   build2=request.GET.get('ipaddress')
   print(build1,build2)
   return render(request, 'services.html',{'build1':build1,'build2':build2})


# def services(request):
#     if request.method == "POST":
#         BuildNumber = request.POST.get('buildno')            
#         ipAdd = request.POST.get('ipaddress')
#         print("hiiiiiiiiiiiiiiii")
#         print("Build_Number :",BuildNumber)
#         print("IP-Addess :",ipAdd)
#         # messages.success(request, 'Your message has been sent.') 
#     return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')            
        Email = request.POST.get('email')
        contact = Contact(name=Name,email=Email,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
