from django.urls import path,include
from . import views

app_name= 'accounts'

urlpatterns = [
    path('sigin/', views.Sigin.as_view(),name='sigin'),
    path('opt/', views.Opt.as_view(),name='opt'),
    path('login/',views.Login.as_view(),name ='login'),
    path('logout/',views.Logout.as_view(), name="Logout"),
    path ('forget/',views.Forget.as_view(),name='forget'),
    path('changepasswor/',views.opcode1.as_view(),name ='opcode1'),
    path('Changepassword/',views.Changepassword.as_view(),name='Changepassword'),
    path('Profile/',views.Prtofile.as_view(),name='Profile')

]

