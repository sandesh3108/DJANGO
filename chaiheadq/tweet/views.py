from django.shortcuts import render
from .models import tweet
from .forms import tweetforms
from django.shortcuts import get_object_or_404

# Create your views here.
def index(req):
    return render(req,'index.html')

# this function is to get all tweets
def tweerlist(req):
    tweets=tweet.objects.all().order_by('-created_at')
    return render(req,'tweet_list.html',{'tweets':tweets})

