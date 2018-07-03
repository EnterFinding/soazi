from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from generic.models import *

class SoaziUserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='重复密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = SoaziBaseUser
		fields = 'email', 'username'
		widgets = {
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
		}
	
	def clean_passwod2(self):
		password1 = self.cleaned_data.get('password1', None)
		password2 = self.cleaned_data.get('password2', None)
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('密码错误!')
		return password2
	
	def save(self, commit=True):
		user = super(SoaziUserCreationForm, self).save(commit=True)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class SoaziUserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()
	
	class Meta:
		model = SoaziBaseUser
		fields = 'email', 'username', 'is_active', 'is_admin'
	
	def clean_password(self):
		return self.initial['password']
