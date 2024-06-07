from django.db.models.signals import post_save
from .models import ProfileUser,User


def create_user(sender,**kwargs):
    if kwargs['created']:
        ProfileUser.objects.create(username=kwargs['instance'])

post_save.connect(receiver=create_user,sender=User)