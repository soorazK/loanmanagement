from django.conf.urls import include,url
from django.urls import path
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url('^formtest$',views.formtest, name="formtest"),
path('', views.dashboard, name="dashboard"),
url('^calculator/$', views.loan_calculator_test, name="loan_calculator"),
url('^check_payments/$', views.check_payments, name='check_payments'),
]
