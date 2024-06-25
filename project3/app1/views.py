from django.shortcuts import render

# Create your views here.
def allapp(req):
    return render(req,'app1/index.html')