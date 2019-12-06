from django.conf.urls import url
from django.conf.urls import include,url
from django.urls import path
from . import views

urlpatterns = [
path(r'', views.dashboard, name="dashboard"),

]
