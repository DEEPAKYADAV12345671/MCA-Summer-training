
from django.contrib import admin
from django.urls import path,include
from .views import registration,login, dashboard

urlpatterns = [
   
    path('registration/', registration ),
    path('login/', login),
    path('dashboard/', dashboard ),
    
]