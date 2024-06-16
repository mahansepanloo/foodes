from django.urls import path,include
from . import views

app_name= 'order'

urlpatterns = [
    path('cart/', views.CartViwe.as_view(),name='cart'),
    path('CartAdd/<int:food_id>',views.CartAdd.as_view(),name='add'),
    path('remove/<int:id_food>',views.CARTremove.as_view(),name='remove'),
    path('order/<int:id_order>', views.ShowOrder.as_view(), name='order'),
    path("add_order/",views.AddOrder.as_view(),name='add_order')

]

