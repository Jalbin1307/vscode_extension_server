from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'rest_api_test'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
    
]