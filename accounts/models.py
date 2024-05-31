import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import Usermanager



class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = Usermanager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']


    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin

class OptCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.IntegerField()
    timeCreate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number}__{self.code}'