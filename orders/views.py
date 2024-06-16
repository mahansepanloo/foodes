from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .cart import Cart
from .forms import add ,off
from home.models import Food
from .models import Order,OrderItem,Coupon
import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from home.forms import SearchForm





class CartViwe(View):
    def get(self,request):
        search =SearchForm()
        cart = Cart(request)
        return render(request,'cart.html',{'cart':cart,'search':search})

class CartAdd(View):
    def post(self,request,food_id):
        cart=Cart(request)
        food = get_object_or_404(Food,id=food_id )
        num = add(request.POST)
        if num.is_valid():
            cd=num.cleaned_data['num']
            cart.add(food,cd)
            return redirect('order:cart')
class CARTremove(View):
    def get(self,request,id_food):
        cart=Cart(request)
        food = get_object_or_404(Food,id=id_food)
        cart.remove(food)
        return redirect('order:cart')

class ShowOrder(LoginRequiredMixin,View):
    def get(self,request,id_order):
        offform = off()
        order = get_object_or_404(Order,id=id_order)
        return render(request,'showorder.html',{'order':order,'off':offform})


    def post(self,request,id_order):
        now = datetime.datetime.now()
        form = off(request.POST)
        if form.is_valid():
            code = form.cleaned_data['off']
            try:
                coupon =Coupon.objects.get(user__exact=request.user ,code__exact=code,
                                            valid_from__lte=now, valid_to__gte=now, active=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'this coupon does not exists', 'danger')
                return redirect('orders:order', id_order)
            order =get_object_or_404(Order,id=id_order)
            order.discount = coupon.discount
            order.save()
            return redirect('order:order', id_order)






class AddOrder(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request,'first log in','success')
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        cart=Cart(request)
        orders = Order.objects.create(user=request.user)
        for item in cart:
             OrderItem.objects.create(order=orders,foods=item['name'],price=item['price'],num=item['num'])
        return redirect('order:order',orders.id)

