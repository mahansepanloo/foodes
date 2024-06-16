from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import Usermanager











class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = Usermanager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']


    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin



class ProfileUser(models.Model):
    firstname = models.CharField(max_length=100,blank=True,null=True,default=' ')
    lastname = models.CharField(max_length=100,blank=True,null=True,default='  ')
    age = models.IntegerField(blank=True,null=True,default='0')
    bio = models.TextField(max_length=100,blank=True,null=True,default='  ')
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    def __str__(self):
        return f'{self.firstname}'



class OptCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.IntegerField()
    timeCreate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number}__{self.code}'