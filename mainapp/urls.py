

from django.urls import path
from .views import (index,about,
scholarship)

app_name = 'mainapp'
urlpatterns = [
    path('', index,name='index'),
    path('about/',about,name='about'),
    path('scholarship/',scholarship,name="scholarship")
  
]
