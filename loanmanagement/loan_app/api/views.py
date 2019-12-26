from rest_framework.generics import (ListAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
CreateAPIView)


import datetime as dt

from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from  ..models import Loantype,Loan,Payment, CustomUser, PasswordReset
from .serializers import LoanSerializer,LoantypeSerializer,PaymentSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter

from ..helpers import LoanCalculator

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
    # permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #pagination_class=LoanLimitOffsetPagination
    filter_backends = (SearchFilter, )
    search_fields = ('status', 'employee_id', 'employee_name')

class LoanDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    lookup_field='employee_id'
    #lookup_url_kwarg==

class LoanUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoanCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    #lookup_field=
    #lookup_url_kwarg==
#api for loantype

class LoantypelistAPIView(ListAPIView):
    authentication_classes = ()
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

class LoantypeDetailAPIView(RetrieveAPIView):
    authentication_classes = ()
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer
    #lookup_field=
    #lookup_url_kwarg==

class LoantypeCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Loantype.objects.all()
    serializer_class=LoantypeSerializer

#api for payment
class PaymentlistAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentDeleteAPIView(DestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    #lookup_field=
    #lookup_url_kwarg==

class PaymentCreateAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class LoginView(APIView):
    authentication_classes = ()
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        if created:
            return Response({"token": token.key}, status=200)
        else:
            token.delete()
            new_token = Token.objects.create(user=user)
            return Response({'token': new_token.key}, status=200)

class UserAddAPIView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_exists = CustomUser.objects.filter(username=serializer.validated_data['username']).exists()

        if user_exists:
            return Response({'msg': 'Username already taken'}, status=409)

        user = CustomUser(
            username = serializer.validated_data['username'],
            email = serializer.validated_data['email'],
            first_name = serializer.validated_data.get('first_name', ''),
            last_name = serializer.validated_data.get('last_name', ''),
            is_staff = serializer.validated_data.get('is_staff', False)
        )

        user.set_password(serializer.validated_data['password'])

        user.save()

        return Response({'msg': 'User created successfully'}, status=201)


class UserUpdateAPIView(UpdateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAdminUser]
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer

    def post(self, request, username):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        current_user = CustomUser.objects.get(username=username)
        if not current_user:
            return Response({'msg': "Not found"}, status=400)

        password = serializer.validated_data.get('password')
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        email = serializer.validated_data.get('email')
        is_staff = serializer.validated_data.get('is_staff')

        current_user.first_name = first_name or current_user.first_name
        current_user.last_name = last_name or current_user.last_name
        current_user.email = email or current_user.email
        current_user.is_staff = current_user.is_staff if is_staff is None else is_staff

        if password:
            current_user.set_password(password)

        current_user.save()

        return Response({"msg": "success"}, status=201)


class LogoutView(APIView):
    authentication_classes = ()
    def post(self, request):
        try:
            return Response({'msg': 'Logout Successful'}, status=200)
        except Exception as e:
            return Response({'msg': 'Logout Failed'}, status=500)

class SendPasswordReset(APIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticated]

    def send_password_reset_email(self, user):
        pass_reset = PasswordReset(user=user, email=user.email)
        pass_reset.save()

        result = pass_reset.send_password_reset()

        if result is False:
            return Response({'msg': 'Password Reset Email could not be sent'}, status=500)
        return Response({'msg': 'Password Reset Email sent.'}, status=200)

    def post(self, request, slug):

        users = CustomUser.objects.filter(username=slug)

        if len(users) <= 0:
            return Response({'msg': 'User not found'}, status=404)

        user = users[0]

        prs = PasswordReset.objects.filter(user=user)

        if len(prs) <= 0:
            return self.send_password_reset_email(user)
        else:
            for pr in prs:
                pr.forced_expired = True
                pr.save()

            return self.send_password_reset_email(user)


class ResetPassword(APIView):
    def get(self, request, slug):

        pass_reset = PasswordReset.objects.filter(key=slug)

        if len(pass_reset) <= 0:
            return Response({'msg': 'Request url not found'}, status=400)

        pr = pass_reset[0]

        if not pr.changed and not pr.forced_expired:
            new_password = request.data['new_password']

            user = pr.user

            user.set_password(new_password)
            user.save()
            pr.changed = True
            pr.save()

            return Response({'msg': 'Password changed'}, status=200)
        else:
            return Response({'msg': 'This url has already been used.'}, status=300)


class CheckToken(APIView):
    authentication_classes = ()

    def post(self, request):
        key = request.data.get('token')

        if key:
            try:
                token = Token.objects.get(key=key)
                return Response({'msg': 'Authentication Token found', 'username': token.user.username}, status=200)
            except:
                return Response({'msg': 'Authentication Token not found', 'username': ''}, status=404)
        return Response({'msg': 'Authentication Token not supplied', 'username': ''}, status=400)


class GetLoanDetail(APIView):
    authentication_classes = ()

    def post(self, request):
        loan_type = request.data.get('loan_type')
        dob = request.data.get('dob')
        loan_amount = request.data.get('loan_amount')
        # mobile_number = request.data.get('mobile_number')

        if not dob or not loan_amount or not loan_type: #or not mobile_number
            return Response({'msg': 'Required information is missing'}, status=400)

        try:
            loan = Loan.objects.get(loanname__loantype=loan_type, DOB=dob, loanamount=loan_amount) #, employee_name=employee_name, mobile_number=mobile_number)
            serializer = LoanSerializer(loan)
            payments = loan.payment_set.all().order_by('-updated_on')
            lc = LoanCalculator(loan.loanamount, loan.loanname.interest, loan.loanname.period_years, loan.loanname.num_payments_per_year, loan.loanname.start_date)
            breakdown = lc.generate_table()

            return Response({'msg': 'Success', 'loan_detail':serializer.data, 'breakdown': breakdown}, status=200)
        except Exception as e:
            return Response({'msg': 'Loan not found', 'loan_detail': {}, 'breakdown': {}}, status=404)



class GetAnalytics(APIView):
    authentication_classes = (TokenAuthentication, )

    response_schema = {
        'msg': '',
        'analytics': {
            'pie_chart': [

            ],
            'line_chart': [

            ],
            'bar_chart': [

            ],
            'forcast_chart': [

            ]
        },
    }

    def post(self, request):
        try:
            today = dt.date.today()
            current_year = today.year
            current_month = today.month

            if current_month == 12:
                start_year = current_year
                start_month = 1
                check_at = [(start_year, i) for i in range(1, current_month + 1)]
            else:
                start_year = current_year - 1
                start_month = current_month + 1
                check_at = [(start_year, i) for i in range(start_month, 13)]
                check_at.append([(current_year, i) for i in range(1, current_month + 1)])

            loan_types = Loantype.objects.all()

            for loan_type in loan_types:
                payment_collection_this_month = 0
                loan_issued_this_month = 0
                loans = loan_type.loan_set.all()
                for loan in loans:
                    if loan.loan_issue_1_status and loan.loan_issue_1_date.year == current_year and loan.loan_issue_1_date.month == current_month:
                        loan_issued_this_month += loan.loan_issue_1_amount
                    if loan.loan_issue_2_status and loan.loan_issue_2_date.year == current_year and loan.loan_issue_2_date.month == current_month:
                        loan_issued_this_month += loan.loan_issue_2_amount

                    payments = loan.payment_set.all()
                    for payment in payments:
                        if payment.payment_date.year == current_year and payment.payment_date.month == current_month:
                            payment_collection_this_month += payment.payment_amount

                self.response_schema.get('analytics').get('bar_chart').append({'name': loan_type.loantype, 'value': loan_issued_this_month})
                self.response_schema.get('analytics').get('pie_chart').append({'name': loan_type.loantype, 'value':payment_collection_this_month})
                self.response_schema.get('analytics').get('forcast_chart').append({'name': loan_type.loantype, 'value': loan.installment_amount})



            for check in check_at:
                month_name = "{}-{}".format(check[0], check[1])
                final_json = {'name': month_name}
                for loan_type in Loantype.objects.all():
                    payments = Payment.objects.filter(loan__loanname__loantype=loan_type, payment_date__year=check[0], payment_date__month=check[1])
                    total_payment_for_checked_month = 0
                    for payment in payments:
                        total_payment_for_checked_month += payment.payment_amount

                    final_json.update({loan_type.loantype: total_payment_for_checked_month})

                self.response_schema.get('analytics').get('line_chart').append(final_json)
                self.response_schema['msg'] = 'Success'
            return Response(self.response_schema, status=200)
        except Exception as e:
            return Response({'msg': 'Failure', 'analytics': {}}, status=500)