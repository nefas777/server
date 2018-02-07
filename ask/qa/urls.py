
from django.conf.urls import patterns, include, url
from . import views

urlpastterns = [
    url(r'^.*$', views.test)
]
