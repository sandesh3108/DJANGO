from django.http import HttpResponse
from django.shortcuts import render 

def home(req):
    # return HttpResponse('welcome home')
    return render(req,'index.html')
