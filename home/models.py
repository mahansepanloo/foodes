from django.db import models
from accounts.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name





class Food(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media\%Y-%m-%d')
    Available = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ofood')
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)


    def total_rate(self):
        return (sum(item.totalrate() for item in self.frate.all() ))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home:about",args=[self.slug,])




class Commit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ucomment')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='fcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    comment = models.TextField()
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='urate')
    rate = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)])
    created = models.DateTimeField(auto_now=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='frate')



    def __str__(self):
        return self.user.username

    def totalrate(self):
        return self.rate

