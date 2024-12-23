from django import forms
from .models import User, ProfileUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import re

# Helper method for password validation
def validate_password(password):
    if len(password) < 5:
        raise ValidationError('Password must be more than 5 characters.')
    if password.isnumeric():
        raise ValidationError('Password must contain letters.')
    if password.isalpha():
        raise ValidationError('Password must contain numbers.')
    if password.islower():
        raise ValidationError('Password must contain uppercase letters.')
    if password.isupper():
        raise ValidationError('Password must contain lowercase letters.')
    return password


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'phone_number')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Duplicate username!')
        return username

    def clean_phone_number(self):
        phonenumber = self.cleaned_data['phone_number']
        if not re.match(r'^09[0-9]{9}$', str(phonenumber)):
            raise ValidationError('Phone number is invalid!')
        if User.objects.filter(phone_number=phonenumber).exists():
            raise ValidationError('Duplicate phone number!')
        return phonenumber

    def clean(self):
        cd = self.cleaned_data
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        validate_password(p1)
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords do not match!')
        return cd

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="You can change password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password', 'last_login')


class Singin_Forms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'phone_number')

    def clean_phone_number(self):
        phonenumber = self.cleaned_data['phone_number']
        if not re.match(r'^09[0-9]{9}$', phonenumber):
            raise ValidationError('Phone number is invalid!')
        if User.objects.filter(phone_number=phonenumber).exists():
            raise ValidationError('Duplicate phone number!')
        return phonenumber

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Duplicate username!')
        return username

    def clean(self):
        cd = self.cleaned_data
        p1 = cd.get('password')
        p2 = cd.get('password2')
        validate_password(p1)
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords do not match!')
        return cd


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
        p1 = cd.get('password')
        p2 = cd.get('password2')
        validate_password(p1)
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords do not match!')
        return cd


class ProfileForms(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['firstname', 'lastname', 'bio', 'age']
