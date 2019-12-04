from django.conf.urls import url
from django.contrib import admin
from .views import (
PaymentlistAPIView,PaymentDetailAPIView,PaymentUpdateAPIView,PaymentDeleteAPIView,PaymentCreateAPIView)
urlpatterns = [
url(r'^$',PaymentlistAPIView.as_view(),name='paymentlist'),
url(r'^(?P<pk>\d+)/$',PaymentDetailAPIView.as_view(),name='paymentdetail'),
url(r'^(?P<pk>\d+)/edit/$',PaymentUpdateAPIView.as_view(),name='paymentupdate'),
url(r'^(?P<pk>\d+)/delete/$',PaymentDeleteAPIView.as_view(),name='paymentdelete'),
url(r'^create/$',PaymentCreateAPIView.as_view(),name='paymentcreate'),
]
