from django.contrib import admin
from .models import Order,OrderItem,Coupon



class OrderIteminline(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('Create',)
    inlines = (OrderIteminline,)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass