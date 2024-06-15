from django.shortcuts import render ,redirect
from django.views import View
from .forms import Singin_Forms , OptForms, LOginForms , ForgetForm,ChangepasswordForm,ProfileForms

from .models import User ,OptCode , ProfileUser
from random import randint
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin











class Sigin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            messages.success(request, 'first log out', 'success')
            return redirect('accounts:Logout')
        return super().dispatch(request, *args, **kwargs)

    randomcod = randint(1000,9999)
    def get(self,request):
        forms = Singin_Forms()
        return render(request,'sing in.html',{'froms':forms})
    def post(self,request):
        forms = Singin_Forms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            info =OptCode.objects.filter(phone_number=cd['phone_number'])
            if info.exists():
                info.delete()
            OptCode.objects.create(code=self.randomcod, phone_number=cd['phone_number'])
            request.session['signin']={
                'username':cd['username'],
                'phone_number':cd['phone_number'],
                'password':cd['password']
            }
            messages.success(request,'opt code sent to phone_number','success')
            return redirect('accounts:opt')
        return render(request,'sing in.html',{'froms':forms})

class Opt(View):
        now = timezone.now()
        def get(self,request):
            formopt= OptForms()
            return render(request,'opt.html',{"forms":formopt})
        def post(self,request):
            formopt = OptForms(request.POST)
            if formopt.is_valid():
                cd = formopt.cleaned_data
                info = OptCode.objects.get(phone_number=request.session['signin']['phone_number'])
                extime = info.timeCreate + timedelta(minutes=1)
                if extime < self.now:
                    messages.error(request,'time opt cod is finesh','success')
                    return redirect('accounts:sigin')
                if extime > self.now and info.code == cd['code']:
                    User.objects.create_user(username=request.session['signin']['username'],
                                             phone_number=request.session['signin']['phone_number'],
                                             password=request.session['signin']['password'])
                    info.delete()
                    messages.success(request,'Registr is succes' , 'success')
                    return redirect('home:home')
                messages.success(request, 'opt not true', 'success')

            return render(request, 'opt.html', {"forms": formopt})
class Login(View):
    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request,'first log out','success')
            return redirect('accounts:Logout')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        forms = LOginForms()
        return render(request,'Login.html',{'forms':forms})

    def post(self,request):
        forms = LOginForms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            u = authenticate(request, username=cd['username'], password=cd['password'])
            if u is not None:
                login(request,u)
                messages.success(request,'welcome','success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, 'Login.html', {'forms': forms})
class Logout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')

class Forget(View):
    randomcod = randint(1000,9999)

    def get(self,request):
        forms = ForgetForm()
        return render(request,'opt.html',{'forms':forms})
    def post(self,request):
        forms = ForgetForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            info = OptCode.objects.filter(phone_number=cd['phone_number'])
            if info.exists():
                info.delete()
            OptCode.objects.create(code=self.randomcod, phone_number=cd['phone_number'])
            request.session['forget']={
                'phone_number' : cd['phone_number']
            }
            return redirect('accounts:opcode1')
        return render(request,'opt.html',{'forms':forms})



class opcode1(View):
    now = timezone.now()
    def get(self, request):
        formopt = OptForms()
        return render(request, 'opt.html', {"forms": formopt})

    def post(self, request):
        formopt = OptForms(request.POST)
        if formopt.is_valid():
            cd = formopt.cleaned_data
            info = OptCode.objects.get(phone_number=request.session['forget']['phone_number'])
            extime = info.timeCreate + timedelta(minutes=1)
            if extime < self.now:
                messages.error(request, 'time opt cod is finesh', 'success')
                return redirect('accounts:forget')
            if extime > self.now and info.code == cd['code']:
                info.delete()
                return redirect('accounts:Changepassword')
            messages.success(request, 'opt not true', 'success')

        return render(request, 'opt.html', {"forms": formopt})




class Changepassword(View):
    def get(self,request):
        forms = ChangepasswordForm()
        return render(request, 'opt.html', {'forms': forms})
    def post(self,request):
        forms = ChangepasswordForm(request.POST)
        if forms.is_valid():
            u = User.objects.get(phone_number=request.session['forget']['phone_number'])
            u.set_password(forms.cleaned_data['password'])
            u.save()
            del request.session['forget']
            messages.success(request,'password change','success')
            return redirect('accounts:login')
        return render(request, 'opt.html', {'forms': forms})

class Prtofile(View):
    def setup(self, request, *args, **kwargs):
        self.info_user = User.objects.get(id=request.user.id)
        self.info_profile = ProfileUser.objects.get(username_id=self.info_user.id)
        return super().setup( request, *args, **kwargs)
    def get(self,request):
        forms = ProfileForms(initial={'phone_number':self.info_user.phone_number},instance=self.info_profile)
        return render(request, 'info.html', {'forms': forms})
    def post(self,request):
        forms = ProfileForms(request.POST,initial={
                             'phone_number': self.info_user.phone_number},
                             instance=self.info_profile)
        if forms.is_valid():
            forms.save()
            forms.phone_number=forms.cleaned_data['phone_number']
            forms.save()
            messages.success(request,'profile is  change','success')
            return redirect('home:home')
        return render(request, 'info.html', {'forms': forms})

