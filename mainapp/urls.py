

from django.urls import path
from .views import (index,about,
scholarship,
user_profile,
edit_profile,
upload_scholarship,
recommendations)

app_name = 'mainapp'
urlpatterns = [
    path('', index,name='index'),
    path('about/',about,name='about'),
    path('scholarship/',scholarship,name="scholarship"),
    path('user_profile/',user_profile,name="user_profile"),
    path('edit_profile/',edit_profile,name="edit_profile"),
    path('upload_scholarship/',upload_scholarship,name="upload_scholarship"),
    path('recommendations/',recommendations,name="recommendations")
  
]
