from.import views
from django.urls import path


urlpatterns = [
    # path('', admin.site.urls),
    path('',views.tweetlist,name='tweetlist'), 
    path('creat/',views.tweetcreat,name='tweetcreat'), 
    path('<int:tweet_id>/edit/',views.tweetedit,name='tweetedit'),
    path('<int:tweet_id>/delet/',views.tweetdelet,name='tweetdelete'),
]
