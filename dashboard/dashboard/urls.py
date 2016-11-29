from django.conf.urls import url

from . import views

app_name = 'dashboard'


urlpatterns = [
	#dash
    url(r'^dash$', views.dashboard, name='dashboard'),
    #config
    url(r'^config$', views.config, name='config'),
    # ex: /dashboard/
    url(r'^$', views.index, name='index'),
	
]