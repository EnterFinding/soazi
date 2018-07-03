from django.conf import settings
from django.db.models import Q

from generic.models import SoaziBaseUser

class SoaziAuthBackend(object):
	
	def authenticate(self, username=None, password=None):
		try:
			user = SoaziBaseUser.objects.get(Q(username=username)|Q(email=username))
			print(user)
		except SoaziBaseUser.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				return user
			return None
		
	def get_user(self, user_id):
		try:
			return SoaziBaseUser.objects.get(pk=user_id)
		except SoaziBaseUser.DoesNotExist:
			return None