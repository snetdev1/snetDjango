from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import logTheUserOut, returnRootLanding, returnUserObject, displayMetaData, social_register



urlpatterns = patterns('',
                       url(r'^sociallogin/', social_register),
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
                       url(r'^here/', include('here.urls')),
                       url(r'^core/', include('core.urls')),

)