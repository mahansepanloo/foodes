from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'home'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('<slug:slug_id>',views.AboutFood.as_view(),name = 'about' )

]
