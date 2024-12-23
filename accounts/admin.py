from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BASEADMIN
from .models import User , OptCode , ProfileUser
from .forms import UserChangeForm,UserCreateForm
from django.contrib.auth.models import Group

@admin.register(OptCode)
class OptCodeAdmin(admin.ModelAdmin):
	list_display = ('code', 'phone_number', 'timeCreate')
	readonly_fields = ('timeCreate',)


class Profline(admin.StackedInline):
    model = ProfileUser


class UserAdmin(BASEADMIN):
	form = UserChangeForm
	add_form = UserCreateForm

	list_display = ('username', 'phone_number', 'is_admin')
	list_filter = ('is_admin',)
	readonly_fields = ('last_login',)

	fieldsets = (
		('Main', {'fields':('username', 'phone_number', 'password')}),
		('Permissions', {'fields':('is_active', 'is_admin', 'last_login','is_superuser','groups','user_permissions')}),
	)

	add_fieldsets = (
		(None, {'fields':('phone_number', 'username',  'password1', 'password2')}),
	)

	search_fields = ('email', 'username')
	ordering = ('username',)

	filter_horizontal = ('user_permissions','groups')

	def get_form(self, request, obj=None, change=False, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		if not request.user.is_superuser:
			form.base_fields['is_superuser'].disabled  = True
		return form


	inlines = (Profline,)
	def get_form(self, request, obj=None, change=False, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		super_users = request.user.is_superuser
		if not super_users:
			form.base_fields['is_superuser'].disabled = True
			form.base_fields['user_permissions'].disabled = True


		return form

admin.site.register(User, UserAdmin)
