from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('aboutus/',aboutus,name='aboutus'),
    path('services/',services,name='services'),
    path('prices/',prices,name='prices'),
    path('teams/',teams,name='teams'),
    path('contacts/',contacts,name='contacts'),
    path('washingPoints/',washingPoints,name='washingPoints'),
    path('blog/',blog,name='blog'),
    path('blogDetails/',blogDetails,name='blogDetails'),
]