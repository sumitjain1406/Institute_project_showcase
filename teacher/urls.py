from django.urls import path 
from . import views

urlpatterns = [
    
    path('',views.teacher),
    path('enrollment/',views.enroll),
    
]