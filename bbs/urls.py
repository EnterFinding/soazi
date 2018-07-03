from django.urls import path

from bbs.views import *
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('category/<str:code>', CategoryView.as_view(), name='category'),
	path('detail/<int:pk>.html', ArticleView.as_view(), name='detail'),
	path('detail/<int:good>/', ArticleView.as_view(), name='detail_good'),
	path('leader/', LeaderView.as_view(), name='leader'),
]