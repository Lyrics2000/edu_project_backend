
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentification.urls')),
    path('',include('mainapp.urls',namespace='mainapp'))
]
