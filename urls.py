from django.conf.urls.defaults import patterns, include, url

from .views import ke_upload_view, ke_man_view

urlpatterns = patterns("",
        url(r'^$', ke_upload_view, name='ke_upload'),
        url(r'^man/$', ke_man_view, name='ke_man'),
        )
