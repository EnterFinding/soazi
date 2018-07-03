from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.db.models import F
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from bbs.models import *
from bbs.forms import *

import json
# Create your views here.

class IndexView(ListView):
	template_name = 'bbs/index.html'
	model = ArticleList
	context_object_name = 'articles'
	
	def get_context_data(self, **kwargs):
		kwargs['codes'] = CodeList.objects.values('code')
		kwargs['newarticle'] = NewArticleForm
		return super(IndexView, self).get_context_data(**kwargs)
	
	def http_method_not_allowed(self, request, *args, **kwargs):
		if request.method == 'POST':
			topic = request.POST['topic']
			description = request.POST['description']
			content = request.POST['content']
			code = request.POST['code']
			author = request.user
			iz = CodeList.objects.get_or_create(code=code)
			article = self.model(topic=topic, description=description, content=content, author=author, code=iz[0])
			article.save()
		return HttpResponseRedirect('/')

class CategoryView(ListView):
	template_name = 'bbs/index.html'
	model = ArticleList
	context_object_name = 'articles'
	
	def get_context_data(self, **kwargs):
		kwargs['codes'] = CodeList.objects.values('code')
		kwargs['newarticle'] = NewArticleForm
		return super(CategoryView, self).get_context_data(**kwargs)
	
	def get_queryset(self):
		code = self.kwargs.get('code', None)
		return super(CategoryView, self).get_queryset().filter(code__code=code)
	
class ArticleView(DetailView):
	template_name = 'bbs/detail.html'
	model = ArticleList
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		kwargs['reply'] = ReplyList.objects.filter(topic=self.kwargs.get('pk')).values('content', 'author', 'created')
		kwargs['replyform'] = ReplyForm
		return super(ArticleView, self).get_context_data(**kwargs)

	def get_object(self, queryset=None):
		kwargs = super(ArticleView, self).get_object(queryset)
		kwargs.visits +=1
		kwargs.save()
		return kwargs

	def http_method_not_allowed(self, request, *args, **kwargs):
		id = self.kwargs.get('good', None)
		if id:
			article = ArticleList.objects.get(id=id)
			if article:
				ck = PushLog.objects.get_or_create(topic=article, username=request.user)
				if ck[1]:
					article.likes += 1
					article.save()
					num = {'over': article.likes}
				else:
					num = {'over': '请勿重复操作!'}
			else:
				num = {'over': '系统发生错误!'}
		return HttpResponse(json.dumps(num), content_type='application/json')

class LeaderView(TemplateView):
	template_name = 'bbs/leader.html'
	
	def get_context_data(self, **kwargs):
		kwargs['hot_leader'] = ArticleList.objects.order_by('-visits')[:10].values('id', 'topic', 'visits')
		kwargs['like_leader'] = ArticleList.objects.order_by('-likes')[:10].values('id', 'topic', 'likes')
		return super(LeaderView, self).get_context_data(**kwargs)
