from django.conf.urls import url
from django.contrib import admin
from .views import (
LoantypelistAPIView,LoantypeDetailAPIView,LoantypeUpdateAPIView,LoantypeDeleteAPIView,LoantypeCreateAPIView)
urlpatterns = [
url(r'^$',LoantypelistAPIView.as_view(),name='typelist'),
url(r'^(?P<pk>\d+)/$',LoantypeDetailAPIView.as_view(),name='typedetail'),
url(r'^(?P<pk>\d+)/edit/$',LoantypeUpdateAPIView.as_view(),name='typeupdate'),
url(r'^(?P<pk>\d+)/delete/$',LoantypeDeleteAPIView.as_view(),name='typedelete'),
url(r'^create/$',LoantypeCreateAPIView.as_view(),name='typecreate'),
]
