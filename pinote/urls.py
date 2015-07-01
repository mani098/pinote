from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# url(r'^$', 'pinote.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', 'login.views.login_view', name='login'),  # index page
	url(r'^', include('login.urls')),  # includes register view and home view
	url(r'^weblinks/', include('weblinks.urls')),
	url(r'^passvault/', include('passvault.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
