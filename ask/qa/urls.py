
from django.conf.urls import *
from . import views

urlpastterns = [
    url(r'^.*$', views.test)
]
