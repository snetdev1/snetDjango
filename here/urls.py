from django.conf.urls import patterns, include, url
from django.contrib import admin
from snet.views import returnRootLanding, displayMetaData
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'parties', views.PartyViewSet)

urlpatterns = patterns('',

                       url(r'^(?i)meta/', displayMetaData),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)