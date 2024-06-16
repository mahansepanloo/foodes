from django.contrib import admin
from .models import Food,Rating,Commit,Category

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Commit)
class Admin(admin.ModelAdmin):
    pass
@admin.register(Rating)
class Admin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass