from django.shortcuts import render
from django.views import View
from .models import Food
from orders.forms import add


class Home(View):
    def get(self,request):
        food = Food.objects.filter(Available=True)
        return render(request,'index.html',{'food':food})

class AboutFood(View):
    def setup(self, request, *args, **kwargs):
        self.food = Food.objects.get(slug=kwargs['slug_id'])
        return super().setup(request, *args, **kwargs)

    def get(self,request,*args, **kwargs):
        form = add()
        return render(request,'about.html',{'food':self.food,'add':form})



