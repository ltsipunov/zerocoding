from .models import Film
from django.forms import ModelForm,TextInput, DateTimeInput, Textarea

class Films_postForm(ModelForm):
	class Meta:
		model = Film
		fields = ['title', 'description', 'review' ]
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
			'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
			'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Обзор'})
		}