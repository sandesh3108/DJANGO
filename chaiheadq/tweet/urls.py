from.import views
from django.urls import path


urlpatterns = [
    # path('', admin.site.urls),
    path('',views.index,name='index'), 
]
