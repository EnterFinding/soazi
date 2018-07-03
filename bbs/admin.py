from django.contrib import admin

from bbs.models import *
from bbs.forms import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	
	list_display = 'topic', 'description', 'code', 'author', 'created'

class PushLogAdmin(admin.ModelAdmin):
	
	list_display = 'topic', 'username'

admin.site.site_header = 'Soazi后台管理'
admin.site.site_title = 'Soazi'
admin.site.register(ArticleList, ArticleAdmin)
admin.site.register(ReplyList)
admin.site.register(LabelList)
admin.site.register(CodeList)
admin.site.register(PushLog, PushLogAdmin)
