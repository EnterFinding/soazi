from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from generic.models import *
from generic.forms import *
from bbs.models import ArticleList as BBSArticleList
# Create your views here.

class SoaziLoginView(LoginView):
	template_name = 'generic/login.html'
	redirect_field_name = '/'
	
	def get_form(self, form_class=None):
		kwargs = super(SoaziLoginView, self).get_form(form_class)
		kwargs.fields['username'].widget.attrs = {"class": "form-control"}
		kwargs.fields['password'].widget.attrs = {"class": "form-control"}
		return kwargs

class SoaziRegisterView(CreateView):
	template_name = 'generic/register.html'
	form_class = SoaziUserCreationForm
	success_url = '/'


class SoaziLogoutView(LogoutView):
	template_name = 'bbs/index.html'
	next_page = '/'

class SoaziManageView(DetailView, LoginRequiredMixin):
	template_name = 'generic/private.html'
	model = SoaziBaseUser
	context_object_name = 'userinfo'
	
	def get_context_data(self, **kwargs):
		kwargs['bbs_articles'] = BBSArticleList.objects.filter(author__id=self.kwargs['pk']).values('id', 'topic',
		                                                                                         'visits', 'likes',
		                                                                                         'created')
		return super(SoaziManageView, self).get_context_data(**kwargs)