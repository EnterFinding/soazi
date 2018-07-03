from django.urls import path

from generic.views import *

urlpatterns = [
	path('login/', SoaziLoginView.as_view(), name='login'),
	path('register/', SoaziRegisterView.as_view(), name='register'),
	path('logout/', SoaziLogoutView.as_view(), name='logout'),
	path('private/<int:pk>/', SoaziManageView.as_view(), name='private'),
]