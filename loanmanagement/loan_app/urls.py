from django.conf.urls import include,url
from django.urls import path
from . import views

urlpatterns = [
url('^formtest$',views.formtest, name="formtest"),
path('', views.dashboard, name="dashboard"),
url('^calculator/$', views.loan_calculator_test, name="loan_calculator"),
url('^check_payments/$', views.check_payments, name='check_payments'),
]
