from cgitb import html
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"Shubham"
    }
    # return HttpResponse("this is message")
    return render(request,'index.html',context)


def about(request):
    return HttpResponse("this is message About")