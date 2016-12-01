from django.conf.urls import url
import dashboard.views as views

app_name = 'dashboard'

'''
inner level of urls, e.g., dashboard/dash , dashboard/config
'''
urlpatterns = [
	#dash
    url(r'^dash$', views.dash, name='dash'),
    #config
    url(r'^config$', views.config, name='config'),
    #data
    url(r'^data$', views.data, name='data'),
    #home
    url(r'', views.index, name='index'),
	
]