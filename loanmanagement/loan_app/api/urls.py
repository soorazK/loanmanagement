from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include,url
from .views import (
LoanlistAPIView,LoanDetailAPIView,LoanUpdateAPIView,LoanDeleteAPIView,LoanCreateAPIView,
 LoantypelistAPIView,LoantypeDetailAPIView,LoantypeUpdateAPIView,LoantypeDeleteAPIView,LoantypeCreateAPIView,
 PaymentlistAPIView,PaymentDetailAPIView,PaymentUpdateAPIView,PaymentDeleteAPIView,PaymentCreateAPIView)#LoanView)


urlpatterns = [
url(r'^loans/$',LoanlistAPIView.as_view(),name='list'),
url(r'^loans/(?P<employee_id>\d+)/$',LoanDetailAPIView.as_view(),name='detail'),
url(r'^loans/(?P<pk>\d+)/edit/$',LoanUpdateAPIView.as_view(),name='update'),
url(r'^loans/(?P<pk>\d+)/delete/$',LoanDeleteAPIView.as_view(),name='delete'),
url(r'^loans/create/$',LoanCreateAPIView.as_view(),name='create'),
url(r'^loantypes/$',LoantypelistAPIView.as_view(),name='typelist'),
url(r'^loantypes/(?P<pk>\d+)/$',LoantypeDetailAPIView.as_view(),name='typedetail'),
url(r'^loantypes/(?P<pk>\d+)/edit/$',LoantypeUpdateAPIView.as_view(),name='typeupdate'),
url(r'^loantypes/(?P<pk>\d+)/delete/$',LoantypeDeleteAPIView.as_view(),name='typedelete'),
url(r'^loantypes/create/$',LoantypeCreateAPIView.as_view(),name='typecreate'),
url(r'^payments/$',PaymentlistAPIView.as_view(),name='paymentlist'),
url(r'^payments/(?P<pk>\d+)/$',PaymentDetailAPIView.as_view(),name='paymentdetail'),
url(r'^payments/(?P<pk>\d+)/edit/$',PaymentUpdateAPIView.as_view(),name='paymentupdate'),
url(r'^payments/(?P<pk>\d+)/delete/$',PaymentDeleteAPIView.as_view(),name='paymentdelete'),
url(r'^payments/create/$',PaymentCreateAPIView.as_view(),name='paymentcreate'),
# url(r'^upload/$', LoanView.as_view(), name='upload')
]
