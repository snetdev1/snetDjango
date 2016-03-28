from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import logTheUserOut, returnRootLanding, returnUserObject, displayMetaData



urlpatterns = patterns('',
                       url(r'^$', returnRootLanding),
                       url(r'^u/', returnUserObject),
                       url(r'^(?i)admin/login/', 'django.contrib.auth.views.login',
                           {'template_name': 'registration/auth.html'}),
                       url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'registration/auth.html'}),

                       url(r'^(?i)admin/logout/$', logTheUserOut),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?i)logout/$', logTheUserOut),

                       url(r'^(?i)meta/', displayMetaData),
                       #url(r'^(?i)vote/', include('vote.urls')),
                       url(r'^api/', include('implementationManager.urls')),



)