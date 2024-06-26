# **1] Activate env file (virtual environment)**
```bash
.venv\Scripts\activate
```

# **2] Install django**
```bash
pip install django
```

# **3] modules in python (Requirments )**
```bash
pip freeze > requirments.txt
```

# **4] Install required modules**
```bash
pip install Pillow
```

# **5] create project using following command**
```bash
django-admin startproject project_name
```
project name : chaiheadq
as you create project , you get same folder again into it.

# **6] open that folder**
```bash
cd project_name
```

# **7] Run the server**
```bash
python manage.py runserver
```

# **8] Stop the server using `ctrl+c`.**

# **9] Do migrations (explore why to do it)**
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

# **10] Creating super user**
```bash
python manage.py createsuperuser
```
```bash
python manage.py runserver
```

# **11] Open the link and search the following :**
`
127.0.0.1:8000/admin
`
login with username and password

# **12] Open `settings.py` in `/chaiheadq` and perform following changes .**
```py
import os
```
## Media Configuration
#### To perform operations on media , add the following code below the `settings.py` file .
```py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```
## Static Files Configuration
#### To perform operations on Static files , add the following code below the `settings.py` file .
#### We insert this code , becuase we can search `CSS`,`JS` files . This static command is inserted as follows in `settings.py` : 
```py
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

# **13] To use above assets (Media,Static) we have to perform some changes in `urls.py` file**
```py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```

# **14] Creating Apps**
```bash
python manage.py startapp tweet
```
- now create `urls.py` file in `tweet` app.
- Now copy all the content in `urls.py` in `chaiheadq` project folder and perform following changes .
        - remove `+ static()...` after `urlpatterns` array .
        - remove or commentout all the content in `urlpatterns` .
        - remove all the imports from the top
- for convinience , create a simple html file in app . 
        - Open `views.py` in app , 
        ```py
            from django.shortcuts import render

            def index(request):
                return render(request,'index.html')
        ``` 
- Now again open `urls.py` file in app , and perform changes as follow : 
```py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]
```

- Open `chaiheadq` folder and open `settings.py` file and put following command : 
```py
INSTALLED_APPS = [
    .
    .
    'tweet',
]
```
This insures that , main project file knows that new app is created .
Now , change in templates in same file : 
```py
TEMPLATES = [
    'DIRS':[os.path.join(BASE_DIRS,'templates')],
]
```
Now create new folder in `chaiheadq` known as templates to store html files. 
`chaiheadq/templates`

- Now open `urls.py` in `chaiheadq` : 
```py
from django.urls import path,include

urlpatterns = [
    .
    .
    path('tweet/',include('tweet.urls'))
]
```
move `templates` folder in `chaiheadq` to `tweet` folder .

# **15] Create a `static` folder in root .**
