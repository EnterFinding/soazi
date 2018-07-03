from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from generic.forms import *

# Register your models here.

class SoaziUserAdmin(UserAdmin):
	form = SoaziUserChangeForm
	add_form = SoaziUserCreationForm
	
	list_display = 'username', 'email', 'is_admin'
	list_filter = 'is_admin',
	fieldsets = (
		('用户信息', {'fields': ('email', 'password')}),
		('个人信息', {'fields': ('username',)}),
		('高级权限', {'fields': ('is_admin',)}),
	)
	
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password1', 'password2'),
		})
	)
	
	search_fields = 'username', 'email'
	ordering = '-is_admin', '-username'
	filter_horizontal = ()

admin.site.register(SoaziBaseUser, SoaziUserAdmin)
admin.site.unregister(Group)