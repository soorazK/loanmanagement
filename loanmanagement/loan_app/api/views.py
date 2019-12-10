from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)

from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from  ..models import Loantype,Loan,Payment
from .serializers import LoanSerializer,LoantypeSerializer,PaymentSerializer, LoginSerializer
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
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer


class LoanDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    lookup_field='employee_id'
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
#api for loantype
class LoantypelistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

class LoantypeDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
#api for payment
class PaymentlistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        django_login(request, user)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)