from django import forms

from bbs.models import *

class NewArticleForm(forms.ModelForm):
	
	class Meta:
		style = {'class': 'form-control'}
		model = ArticleList
		fields = 'topic', 'description', 'code', 'content'
		widgets = {
			'topic': forms.TextInput(attrs=style),
			'description': forms.TextInput(attrs=style),
			'code': forms.TextInput(attrs=style),
			'content': forms.Textarea(attrs={'class': 'sr-only'})
		}
		
	def __init__(self, *args, **kwargs):
		super(NewArticleForm, self).__init__(*args, **kwargs)
		self.fields['code'].empty_label = None
	
		

class ReplyForm(forms.ModelForm):
	
	class Meta:
		style = {'class': 'form-control'}
		model = ReplyList
		fields = 'content',