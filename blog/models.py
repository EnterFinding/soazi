from django.db import models

from generic.models import SoaziBaseUser

# Create your models here.
'''
class ArticleList(models.Model):
	
	topic = models.CharField(verbose_name='标题', max_length=128)
	content = models.TextField(verbose_name='内容')
	author = models.ForeignKey(SoaziBaseUser, verbose_name='作者', on_delete=models.CASCADE, related_name='blog_author')
	
	visits = models.PositiveSmallIntegerField(verbose_name='浏览数量', default=0)
	likes = models.PositiveSmallIntegerField(verbose_name='点赞数量', default=0)
	
	created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
	
	class Meta:
		db_table = 'blog_article'
		verbose_name = verbose_name_plural = '文章列表'
	
	def __str__(self):
		return self.topic
'''