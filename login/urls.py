from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^login/$', views.login_view, name='login'),
	url(r'^home/', views.home_view, name='home'),
	url(r'^get-user/', views.get_user, name='get user'),
	url(r'^logout/$', views.logout_view, name='logout'),
	)
