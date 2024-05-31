from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField





class Usercreateform(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','phone_number')
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('نام کاربری تکراری است')
        return username
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phonenumber).exists():
            raise ValidationError('شماره تماس تکراری است')
        return phonenumber

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match')
        return cd['password2']

    def ave(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")

    class Meta:
	    model = User
	    fields = ('username','phone_number','password', 'last_login')



class Singin_Forms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','phone_number')

    def clean(self):
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['password2']
        if p1 and p2 and p1 != p2 :
            raise ValidationError('passwords dont match')
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Duplicate username')
        return username
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phonenumber).exists():
            raise ValidationError('Duplicate phone number')
        return phonenumber


class OptForms(forms.Form):
        code = forms.IntegerField()

class LOginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class ForgetForm(forms.Form):
    phone_number = forms.CharField(max_length=11)

class ChangepasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise ValidationError('passwords dont match')
