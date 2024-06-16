from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Food,Commit,Rating,Category
from orders.forms import add,rateandcommentform,replycomment
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.forms import SearchForm





class Home(View):
    def get(self,request,cat=None):
        search = SearchForm()
        catgory = Category.objects.filter(is_sub=False)
        food = Food.objects.filter(Available=True)
        if request.GET.get('search'):
            food = Food.objects.filter(name__icontains=request.GET['search'])

        if cat:
            catgorys = get_object_or_404(Category,id=cat)
            food=food.filter(category=catgorys)
        return render(request,'index.html',{'food':food,'category':catgory,'search':search})

class AboutFood(View):
    def setup(self, request, *args, **kwargs):
        self.food = get_object_or_404(Food,slug=kwargs['slug_id'])
        self.rate = Rating.objects.filter(food__slug=kwargs['slug_id']).count()
        self.comment = Commit.objects.filter(food__slug=kwargs['slug_id'],is_reply=False)
        return super().setup(request, *args, **kwargs)

    def get(self,request,*args, **kwargs):
        search = SearchForm()
        formadd = add()
        formrate = rateandcommentform()
        if self.food.total_rate() != 0:
            total_rataing = round(self.food.total_rate()/self.rate,2)
        else:
            total_rataing ="-"

        reply = replycomment()
        return render(request,'about.html',{'food':self.food,'add':formadd,
                                        'form':formrate,'total_rataing':total_rataing,'replyc':reply
                                            ,"comment":self.comment,'search':search})
    @method_decorator(login_required)
    def post(self,request,*args, **kwargs):
        formrate = rateandcommentform(request.POST)
        if formrate.is_valid():
            cd = formrate.cleaned_data
            Commit.objects.create(user=request.user,food=self.food,comment=cd['comment'])
            Rating.objects.create(user=request.user,food=self.food,rate=cd['rate'])
            messages.success(request,'tnx','success')
            return redirect('home:about',self.food.slug)






class Reply(LoginRequiredMixin,View):
    def post(self,request,slug_id,comment_id):
        food = get_object_or_404(Food,slug=slug_id)
        comment = get_object_or_404(Commit,id=comment_id)
        reply = replycomment(request.POST)
        if reply.is_valid():
            cd = reply.cleaned_data
            Commit.objects.create(user=request.user,food=food,comment=cd['replycomment'],
                                  is_reply=True,reply=comment)
            return redirect('home:about',food.slug)



