from django.urls import path

from . import  views

urlpatterns = [
    path('', views.HomePageViev.as_view(), name='home'),
    path('about/', views.AboutPageViev.as_view(), name='about')
]