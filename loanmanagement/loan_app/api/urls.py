from django.conf.urls import url
from django.contrib import admin
from .views import (
LoanlistAPIView,LoanDetailAPIView,LoanUpdateAPIView,LoanDeleteAPIView,LoanCreateAPIView)
urlpatterns = [
url(r'^$',LoanlistAPIView.as_view(),name='list'),
url(r'^(?P<pk>\d+)/$',LoanDetailAPIView.as_view(),name='detail'),
url(r'^(?P<pk>\d+)/edit/$',LoanUpdateAPIView.as_view(),name='update'),
url(r'^(?P<pk>\d+)/delete/$',LoanDeleteAPIView.as_view(),name='delete'),
url(r'^create/$',LoanCreateAPIView.as_view(),name='create'),
]
