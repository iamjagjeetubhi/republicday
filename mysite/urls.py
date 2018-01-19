from django.conf.urls import include, url, handler404
from django.contrib import admin
# Static helper function only for development!
from django.conf.urls.static import static
from django.conf import settings
from . import views
from links import views



from django.contrib.auth import views as auth_views
handler404 = 'links.views.index'


urlpatterns = [

    url(r'^user/$', views.userlink, name='user'),
    url(r'^(?P<username>([^/]+))/$', views.myprofileview, name="myprofileview"),
    url(r'^$', views.index, name="indexview"),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
