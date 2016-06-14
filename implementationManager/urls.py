from django.conf.urls import patterns, url, include
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = patterns('implementationManager.views',

                       #url(r'^$', 'displayMetaData'),

                       url(r'^(?i)meta/$', 'displayMetaData'),

                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)


