from django.urls import path
from app2.views import *
app_name='anything2'
urlpatterns=[
    path('a2/',a2,name='a2'),
]