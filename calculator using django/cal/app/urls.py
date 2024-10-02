from django.urls import path
from . import views

urlpatterns = [
     path('home', views.home,name="home1"),
     path('', views.calcultor),

]