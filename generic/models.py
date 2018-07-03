from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
)

# Create your models here.

class SoaziUserManager(BaseUserManager):
	
	def create_user(self, email, username, password=None):
		if not username:
			raise ValueError('请输入正确的用户名!')
		user = self.model(
			email=self.normalize_email(email),
			username=username
		)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=email,
			username=username,
			password=password
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class SoaziBaseUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='用户邮箱', max_length=128, unique=True)
	username = models.CharField(verbose_name='用户名', max_length=12)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	
	created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
	
	objects = SoaziUserManager()
	
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = 'username',
	
	class Meta:
		unique_together = 'email', 'username'
		db_table = 'user'
		verbose_name = verbose_name_plural = '用户列表'
	
	def __str__(self):
		return self.username
	
	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_label):
		return True
	
	@property
	def is_staff(self):
		return self.is_admin

