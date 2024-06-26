from django.shortcuts import render
from .models import tweet
from .forms import tweetforms
from django.shortcuts import get_object_or_404 , redirect

# Create your views here.
def index(req):
    return render(req,'index.html')

# this function is to get all tweets
def tweetlist(req):
    tweets=tweet.objects.all().order_by('-created_at')
    return render(req,'tweet_list.html',{'tweets':tweets})

def tweetcreat(req):
    if req.method=='POST':
        form=tweetforms(req.POST,req.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=req.user
            tweet.save()
            return redirect('tweetlist')
    else:
        form=tweetforms()#import in above

    return render(req,'tweet_form.html',{'form':form})

def tweetedit(req,tweet_id):
    tweet=get_object_or_404(tweet,pk=tweet_id,user=req.user)
    if req.method =='POST':
        form=tweetforms(req.POST,req.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user=req.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form=tweetforms(instance=tweet)

    return render(req,'tweet_form.html',{'form':form})

def tweetdelet(req,tweet_id):
    tweets=get_object_or_404(tweet,pk=tweet_id,user=req.user)
    if req.method == 'POST':
        tweets.delete()
        return redirect('tweetlist')
    return render(req,'tweet_comfirm_delete.html',{'tweet':tweets})

# .save(),delete() is inbuld function in django
