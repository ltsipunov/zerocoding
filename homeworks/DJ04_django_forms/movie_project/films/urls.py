from django.urls import path
from . import views

urlpatterns = [
	path('', views.films, name='films'),
	path('fill', views.fill, name='fill')
]