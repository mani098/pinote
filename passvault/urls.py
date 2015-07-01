from django.conf.urls import patterns, url

from passvault import views

urlpatterns = patterns('',
	url(r'^$', views.passvault_view, name='passvault'),
	url(r'^updatedata/$', views.passvault_form_update, name='passvault_save')
	)
