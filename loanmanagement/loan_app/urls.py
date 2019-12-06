from django.conf.urls import url

from . import views

urlpatterns = [
url('^$', views.dashboard, name="dashboard"),
url('^calculator/$', views.loan_calculator_test, name="loan_calculator")
]
