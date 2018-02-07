from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', include('qa.urls')),
    url(r'^login/', include('qa.urls')),
    url(r'^signup/', include('qa.urls')),
    url(r'^question/(\d+)', include('qa.urls')),
    url(r'^ask/.*$', include('qa.urls')),
    url(r'^popular/', include('qa.urls')),
    url(r'^new/', include('qa.urls')),
]
#urlpatterns = [
#    url(r'^$', 'qa.views.test'),
#    url(r'^login/.*$', 'qa.views.test'),
#    url(r'^signup/.*', 'qa.views.test'),
#    url(r'^question/\d+/$', 'qa.views.test'),
#    url(r'^ask/.*$', 'qa.views.test'),
#    url(r'^popular/.*$', 'qa.views.test'),
#    url(r'^new/.*$', 'qa.views.test'),
#]
