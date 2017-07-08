from django.conf.urls import url
from . import views

app_name = 'sarpenstein'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'register', views.register, name='register'),
	url(r'login', views.login, name='login'),
	url(r'result', views.search, name='search'),
	url(r'search', views.product, name='search-page'),
]