from django import template

from bbs.models import *
register = template.Library()


def get_num(value):
	return ReplyList.objects.filter(topic=value).count()

register.filter('reply_num', get_num)