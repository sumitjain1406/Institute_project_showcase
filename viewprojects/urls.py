from django.urls import path 
from . import views

urlpatterns = [
    
   path("", views.view_projects),
   path("search/", views.search),
   path("all/", views.all),
]