1] Open `templates` folder in app . 
- Create all required HTML files by using reference of `views.py` in app.
- Copy `index.html` content to all html files and change content using jinja template .

- Tweet_list.html
```html
{% extends "layout.html" %}

{% block title %}
Chai Aur Tweet
{% endblock %}

{% block content %}
<a class="btn btn-primary" href="{% url 'tweetcreate' %}">Create a tweet</a>

<div class="container row gap-3">
    {% for tweet in all_tweets %}
    <div class="card" style="width: 18rem;">
        <img src="{{tweet.photo.url}}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{{tweet.user.username}}</h5>
          <p class="card-text">{{tweet.text}}</p>
          <a href="{% url 'tweet_edit' tweet.id %}" class="btn btn-primary">Edit</a>
          <a href="{% url 'tweet_delete' tweet.id %}" class="btn btn-danger">Delete</a>
        </div>
      </div>
    {% endfor %}
</div>
{% endblock %}
```

- Open `urls.py` in app and edit : 
- 