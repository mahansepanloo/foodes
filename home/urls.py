from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'home'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('<slug:slug_id>',views.AboutFood.as_view(),name ='about'),
    path("reply/<slug:slug_id>/<int:comment_id>", views.Reply.as_view(), name='reply'),
    path('cat/<int:cat>',views.Home.as_view(),name='cat')

]
