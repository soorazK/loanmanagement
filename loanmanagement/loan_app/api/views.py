from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from  ..models import Loantype,Loan,Payment
from .serializers import LoanSerializer,LoantypeSerializer,PaymentSerializer
from rest_framework.permissions import IsAuthenticated

#api for loan

# class LoanView(APIView):
#     parser_classes = (FileUploadParser, )
#     def post(self, request, *args, **kwargs):
#         loan_serializer = LoanSerializer(data=request.data)
#
#         if loan_serializer.is_valid():
#             loan_serializer.save()
#             return Response(loan_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanlistAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer


class LoanDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    lookup_field='employee_id'
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
#api for loantype
class LoantypelistAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

class LoantypeDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
#api for payment
class PaymentlistAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
