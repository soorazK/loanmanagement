from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)
from  ..models import Loantype,Loan
from .serializers import LoanSerializer,LoantypeSerializer

class LoanlistAPIView(ListAPIView):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class LoanDetailAPIView(RetrieveAPIView):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
