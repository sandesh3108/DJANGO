from django.http import HttpResponse 

def home(request):
    return HttpResponse("hello,home")

def about(request):
    return HttpResponse("hello,about")
        