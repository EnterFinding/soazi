from django.db import models

from generic.models import SoaziBaseUser
# Create your models here.

class CodeList(models.Model):
	
	code = models.CharField(verbose_name='语言', max_length=12)
	
	created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	
	class Meta:
		db_table = 'bbs_code'
		verbose_name = verbose_name_plural = '语言分类'
	
	def __str__(self):
		return self.code


class ArticleList(models.Model):
	topic = models.CharField(verbose_name='标题', max_length=128)
	description = models.CharField(verbose_name='描述', max_length=256)
	content = models.TextField(verbose_name='内容')
	author = models.ForeignKey(SoaziBaseUser, verbose_name='作者', on_delete=models.CASCADE)
	code = models.ForeignKey(CodeList, verbose_name='分类', on_delete=models.CASCADE)
	
	visits = models.PositiveIntegerField(verbose_name='浏览数量', default=0)
	likes = models.PositiveIntegerField(verbose_name='点赞数量', default=0)
	
	created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
	
	class Meta:
		db_table = 'bbs_article'
		verbose_name = verbose_name_plural = '文章列表'
	
	def __str__(self):
		return self.topic


class ReplyList(models.Model):
	topic = models.ForeignKey(ArticleList, verbose_name='标题', on_delete=models.CASCADE)
	content = models.CharField(verbose_name='内容', max_length=512)
	author = models.ForeignKey(SoaziBaseUser, verbose_name='作者', on_delete=models.CASCADE)
	likes = models.PositiveIntegerField(verbose_name='点赞数量')
	
	created = models.DateTimeField(verbose_name='回复时间', auto_now_add=True)
	
	class Meta:
		db_table = 'bbs_reply'
		verbose_name = verbose_name_plural = '回复列表'
	
	def __str__(self):
		return self.topic.topic


class LabelList(models.Model):
	topic = models.ForeignKey(ArticleList, verbose_name='标题', on_delete=models.CASCADE)
	label = models.CharField(verbose_name='标签', max_length=24)
	
	created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	
	class Meta:
		db_table = 'bbs_label'
		verbose_name = verbose_name_plural = '标签列表'
	
	def __str__(self):
		return self.topic.topic


class PushLog(models.Model):
	username = models.ForeignKey(SoaziBaseUser, verbose_name='用户名', on_delete=models.CASCADE)
	topic = models.ForeignKey(ArticleList, verbose_name='文章', on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'pushlog'
		verbose_name = verbose_name_plural = '操作记录'
	
	def __str__(self):
		return self.username.username