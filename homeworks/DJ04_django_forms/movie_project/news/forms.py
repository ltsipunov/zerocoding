from .models import News_post
from django.forms import ModelForm,TextInput, DateTimeInput, Textarea, HiddenInput

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['pub_date','title', 'short_description', 'text','user' ]
		widgets = {
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата','type': 'datetime-local'}),
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Полный текст новости'}),
			'user': HiddenInput(),
		}