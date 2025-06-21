from .models import News_post
from django.forms import ModelForm,TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['pub_date','user','title', 'short_description', 'text' ]
		widgets = {
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата','type': 'datetime-local'}),
			'user': TextInput(attrs={'class': 'form-control', 'placeholder': 'Пользователь'}),
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Полный текст новости'})
		}