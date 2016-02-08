from django.conf.urls import patterns, url


urlpatterns = patterns('implementationManager.views',

    url(r'^$', 'displayMetaData'),

    url(r'^(?i)test/$', 'returnMetaDataAsJSON'),


)


