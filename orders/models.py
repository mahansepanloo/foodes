from django.db import models
from accounts.models import User
from home.models import Food
from django.core.validators import MinValueValidator, MaxValueValidator

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uorder')
    paied = models.BooleanField(default=False)
    Create = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.user.username

    def total_price(self):
        total = sum(item.total() for item in self.oorderitem.all())
        if self.discount:
            total = (total * self.discount) / 100
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='oorderitem')
    foods = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='forderitem')
    price = models.IntegerField()
    num = models.IntegerField(default=1)

    def total(self):
         return self.price * self.num


class Coupon(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='ucopoun')
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username