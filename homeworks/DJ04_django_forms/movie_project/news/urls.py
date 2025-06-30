from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='news_home'),
	path('fill', views.fill, name='news_fill'),
	path('details/<int:id_value>/', views.details, name='news_details')
]