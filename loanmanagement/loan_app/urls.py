from django.conf.urls import url
from django.contrib import admin
from loan_app.views import (
LoantypelistAPIView,LoantypeDetailAPIView,LoantypeUpdateAPIView,LoantypeDeleteAPIView,LoantypeCreateAPIView)
urlpatterns = [
url(r'^$',LoantypelistAPIView.as_view(),name='list'),
url(r'^(?P<pk>\d+)/$',LoantypeDetailAPIView.as_view(),name='detail'),
url(r'^(?P<pk>\d+)/edit/$',LoantypeUpdateAPIView.as_view(),name='update'),
url(r'^(?P<pk>\d+)/delete/$',LoantypeDeleteAPIView.as_view(),name='delete'),
url(r'^create/$',LoantypeCreateAPIView.as_view(),name='create'),
]
