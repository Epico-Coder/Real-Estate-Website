from django.urls import path
from BlueSkyMainApp import views

urlpatterns = [
    path('', views.home, name='home'),
]
