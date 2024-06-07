from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BASEADMIN
from .models import User , OptCode , ProfileUser
from .forms import UserChangeForm,Usercreateform
from django.contrib.auth.models import Group

@admin.register(OptCode)
class OptCodeAdmin(admin.ModelAdmin):
	list_display = ('code', 'phone_number', 'timeCreate')
	readonly_fields = ('timeCreate',)


class Profline(admin.StackedInline):
    model = ProfileUser


class UserAdmin(BASEADMIN):
	form = UserChangeForm
	add_form = Usercreateform

	list_display = ('username', 'phone_number', 'is_admin')
	list_filter = ('is_admin',)
	readonly_fields = ('last_login',)

	fieldsets = (
		('Main', {'fields':('username', 'phone_number', 'password')}),
		('Permissions', {'fields':('is_active', 'is_admin', 'last_login', )}),
	)

	add_fieldsets = (
		(None, {'fields':('phone_number', 'username',  'password1', 'password2')}),
	)

	search_fields = ('email', 'username')
	ordering = ('username',)
	filter_horizontal = ()

	inlines = (Profline,)


admin.site.register(User, UserAdmin)
