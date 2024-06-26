# **1] `Layout.html` is kept in `templates` folder in root folder.**
- We create a base layout for all html files in our project .

# 2] **`layout.html`**
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
            Chai Tweet
        {% endblock %}
    </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```
- Inject navbar from bootstrap .
```HTML
{% load static %}
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
            Chai Tweet
        {% endblock %}
    </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">DjangoTweet</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

# 3] **Bootstrap**
- Give link address
```HTML
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
```

# 4] **Open `index.html` in `tweet`.**
- Clear all the content in `index.html` So that we can work as per `layout.html`. 
- `index.html`
```HTML
{% extends "layout.html" %}

{% block title %}
Chai Aur Tweet
{% endblock %}

{% block content %}
<h1 class="text-center">Welcome to Django tweet</h1>
{% endblock %}
```

# 5] **Open `models.py` from app(tweet)**
- Add at top , Users in database come from this code
```py
from django.contrib.auth.models import User
```

- Create class as below : 
```py
class tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='tweetPhotos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:15]}..'
```

Now open terminal and run command : 
```bash 
python -m pip install Pillow
```

As we added requirment , add it to `requirement.txt` file .
```bash
pip freeze > requirement.txt
```

We created model , Now migrate it
```bash
python manage.py makemigrations tweet(app_name)
```
```bash 
python manage.py migrate
```

# 6]**Open `admin.py`**
```py
from django.contrib import admin
from .models import tweet
# Register your models here.

admin.site.register(tweet)
```

# 7]**Create `forms.py` in Tweet**
- import djangos forms
```py
from django import forms
from .models import tweet

class TweetForms(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text','photo']
```

# 8]**Open `views.py` in `tweet` folder.**
```py
from django.shortcuts import render
from .models import tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
# landing page
def index(request):
    return render(request,'index.html')

# To list all the tweets
def tweet_list(req):
    all_tweets = tweet.objects.all().order_by('-created_at')
    return render(req,'tweet_list.html',{'tweets':all_tweets})

def create_from(req):
    if req.method=='POST':
        form = TweetForms(req.POST,req.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms()
    return render(req,'tweet_form.html',{'form':form})

def tweet_edit(req,tweet_id):
    tweet = get_object_or_404(tweet,pk=tweet_id,user=req.user)
    if req.method=='POST':
        form = TweetForms(req.POST,req.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet)
    return render(req,'tweet_form.html',{'form':form})

def tweet_del(req,tweet_id):
    tweet = get_object_or_404(tweet,pk=tweet_id,user=req.user)
    if req.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(req,'tweet_confirm_delete.html',{'tweet':tweet})
```