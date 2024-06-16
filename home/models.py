from django.db import models
from accounts.models import User
from django.urls import reverse

class Food(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media\%Y-%m-%d')
    Available = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ofood')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home:about",args=[self.slug,])
