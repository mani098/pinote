from django.conf.urls import patterns, url

from weblinks import views

urlpatterns = patterns('',
	url(r'^$', views.weblinks_view, name='weblinks'),
	)
