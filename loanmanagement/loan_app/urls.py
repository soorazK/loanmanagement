from django.conf.urls import url
from django.conf.urls import include,url
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
url('^formtest$',views.formtest, name="formtest")
path(r'', views.dashboard, name="dashboard"),
]
